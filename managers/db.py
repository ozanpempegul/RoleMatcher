# db_manager.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError
from common.imports.log import *
import os
from models.job import Job, Sites
from PySide6.QtCore import Signal, QObject

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()

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
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)
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
            print("url: ", job.url)

            db.add(job)
            try:
                db.commit()
                print(f"Saved job: {job.title} ({job.url})")
            except IntegrityError:
                db.rollback()
                print(f"Skipped job (duplicate or error): {job.url}")

        self.signal_data_saved.emit()
        db.close()

    def get_jobs(self, skip: int = 0, limit: int = 100) -> list[Job]:
        try:
            logging.info("Getting jobs from the database")
            db = self.SessionLocal()
            jobs = db.query(Job).offset(skip).limit(limit).all()
            db.close()
            print(f"Retrieved {len(jobs)} jobs from the database")
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
            if job:
                db.delete(job)
                db.commit()
                print(f"Removed job with ID {job_id}")
                self.signal_data_saved.emit()
            else:
                print(f"No job found with ID {job_id}")
            db.close()
        except Exception as e:
            logging.error(f"Error removing job with ID {job_id}: {e}")

db_manager = DBManager()  # Module-level instance