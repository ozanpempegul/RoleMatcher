from jobspy import scrape_jobs
from models.job_fetcher_config import JobScraperConfig


class JobFetcher:
    def __init__(self):
        pass

    @classmethod
    def apply_config(self, config: JobScraperConfig):
        self.config = config

    @classmethod
    def fetch_jobs(self):
        config: JobScraperConfig = self.config
        jobs = scrape_jobs(
            site_name=config.site_names,
            search_term=config.search_term,
            location=config.location,
            results_wanted=config.results_wanted,
            hours_old=config.hours_old,
            linkedin_fetch_description=config.linkedin_fetch_description,
        )
        return jobs


job_fetcher = JobFetcher()  # Module-level instance
