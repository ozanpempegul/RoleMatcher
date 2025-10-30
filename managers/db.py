# db_manager.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError
from common.imports.log import *
import os
from models.job import Job, Sites
from models.job_match_score import JobMatchScore
from PySide6.QtCore import Signal, QObject
from pathlib import Path



USE_SQLITE_FLAG = os.getenv("USE_SQLITE", "False").lower() in ("true")
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "./job_alerts.db")
POSTGRES_CONFIG_PRESENT = all(os.getenv(k) for k in ("POSTGRES_DB","POSTGRES_USER","POSTGRES_PASSWORD","POSTGRES_HOST","POSTGRES_PORT"))


def _choose_db_url():
    if USE_SQLITE_FLAG or not POSTGRES_CONFIG_PRESENT:
        sqlite_file = Path(SQLITE_DB_PATH).expanduser().resolve()
        return f"sqlite:///{sqlite_file}", True
    # fallback to postgres
    db = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    pw = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    return f"postgresql+psycopg://{user}:{pw}@{host}:{port}/{db}", False


SQLALCHEMY_DATABASE_URL, _USE_SQLITE = _choose_db_url()
Base = declarative_base()


def _make_engine(**engine_kwargs):
    """Create SQLAlchemy engine. Accepts optional engine kwargs (pool_size, max_overflow, etc.)
    and ensures sqlite gets connect_args={'check_same_thread': False}."""
    if _USE_SQLITE:
        connect_args = {"check_same_thread": False}
        # merge any provided connect_args
        if "connect_args" in engine_kwargs:
            user_ca = engine_kwargs.pop("connect_args")
            if isinstance(user_ca, dict):
                connect_args.update(user_ca)
        return create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args, **engine_kwargs)
    return create_engine(SQLALCHEMY_DATABASE_URL, **engine_kwargs)


site_map = {
    "indeed": Sites.INDEED,
    "linkedin": Sites.LINKEDIN,
    "zip_recruiter": Sites.ZIP_RECRUITER,
    "google": Sites.GOOGLE
}



# python
class DBManager(QObject):
    signal_data_saved = Signal()


    def __init__(self):
        super().__init__()
        # pass engine options as kwargs to _make_engine
        self.engine = _make_engine(pool_size=10, max_overflow=20)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)


    def save_jobs(self, df):
        logging.info("Saving jobs to the database")
        db = self.SessionLocal()
        for _, row in df.iterrows():
            site_enum = site_map.get(row['site'].lower())
            if not site_enum:
                continue

            job = Job(
                site=site_enum,
                url=row.get("job_url") or row.get("job_url_direct"),
                title=row.get("title", "No Title"),
                company_name=row.get("company", "Unknown"),
                location=row.get("location", "Unknown"),
                job_type=row.get("job_type"),
                is_remote=row.get("is_remote", False),
                job_level=row.get("job_level"),
                description=row.get("description")
            )

            db.add(job)
            try:
                db.commit()
            except IntegrityError:
                db.rollback()

        self.signal_data_saved.emit()
        db.close()


    def get_jobs(self, skip: int = 0, limit: int = 100) -> list[Job]:
        try:
            logging.info("Getting jobs from the database")
            db = self.SessionLocal()
            jobs = db.query(Job).offset(skip).limit(limit).all()
            db.close()
            result_jobs = []
            for job in jobs:
                try:
                    _ = Job()
                    _.id = job.id
                    _.site = job.site
                    _.title = job.title
                    _.company_name = job.company_name
                    _.location = job.location
                    _.job_type = job.job_type
                    _.is_remote = job.is_remote
                    _.job_level = job.job_level
                    _.description = job.description
                    _.url = job.url
                    result_jobs.append(_)
                except Exception as e:
                    logging.error(f"Error processing job {job.id}: {e}")
                    continue
            return result_jobs
        except Exception as e:
            logging.error(f"Error retrieving jobs: {e}")
            return []
        
        
    def remove_job(self, job_id: int):
        try:
            logging.info(f"Removing job with ID {job_id} from the database")
            db = self.SessionLocal()
            job = db.query(Job).filter(Job.id == job_id).first()
            job_match = db.query(JobMatchScore).filter(JobMatchScore.job_id == job_id).first()
            if job_match:
                db.delete(job_match)
            if job:
                db.delete(job)
                db.commit()
                self.signal_data_saved.emit()
            db.close()
        except Exception as e:
            logging.error(f"Error removing job with ID {job_id}: {e}")


    def save_match_score(self, job_id: int, score: float):
        """Save or update match score for a given job_id."""
        db = self.SessionLocal()
        try:
            match = db.query(JobMatchScore).filter(JobMatchScore.job_id == job_id).first()
            if match:
                match.score = score
            else:
                match = JobMatchScore(job_id=job_id, score=score)
                db.add(match)
            db.commit()
        except Exception as e:
            logging.error(f"Error saving match score for job {job_id}: {e}")
            db.rollback()
        finally:
            db.close()


    def get_match_score(self, job_id: int) -> float | None:
        """Retrieve the match score for a given job_id. Returns None if not found."""
        db = self.SessionLocal()
        try:
            match = db.query(JobMatchScore).filter(JobMatchScore.job_id == job_id).first()
            return match.score if match else None
        except Exception as e:
            logging.error(f"Error retrieving match score for job {job_id}: {e}")
            return None
        finally:
            db.close()


db_manager = DBManager()  # Module-level instance