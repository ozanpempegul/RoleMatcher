from dotenv import load_dotenv
from managers.db import Base, DBManager
from managers.job_fetcher import JobFetcher
from models.job_fetcher_config import JobScraperConfig



if __name__ == "__main__":
    # init env
    load_dotenv()

    # init database
    db_manager = DBManager()

    # fetch jobs
    job_fetcher = JobFetcher()
    config = JobScraperConfig()
    job_fetcher.apply_config(config)
    jobs = job_fetcher.fetch_jobs()

    # save jobs
    db_manager.save_jobs(jobs)  # Use the manager's method

    print(f"Saved jobs to the database")

    # get jobs
    retrieved_jobs = db_manager.get_jobs()
    print(f"Retrieved {len(retrieved_jobs)} jobs from the database")
