import re
from enum import Enum
from urllib.parse import parse_qs, urlparse

import pandas as pd
from bs4 import BeautifulSoup

from jobspy.linkedin import LinkedIn
from jobspy.linkedin.util import is_job_remote
from jobspy.model import Country, DescriptionFormat, JobPost, Location, ScraperInput, Site
from jobspy.util import desired_order, extract_emails_from_text
from jobspy.ziprecruiter import ZipRecruiter


class JobLinkSite(str, Enum):
    LINKEDIN = "linkedin"
    INDEED = "indeed"
    ZIP_RECRUITER = "zip_recruiter"


_LINKEDIN_PATTERN = re.compile(
    r"linkedin\.com/jobs/view/(?:[\w%-]*-)?(\d+)", re.IGNORECASE
)
_INDEED_PATTERN = re.compile(
    r"indeed\.com/viewjob\?.*\bjk=([a-f0-9]+)", re.IGNORECASE
)
_ZIP_RECRUITER_PATTERN = re.compile(r"ziprecruiter\.com/", re.IGNORECASE)


def parse_job_url(url: str) -> tuple[JobLinkSite, str]:
    url = url.strip()
    if not url:
        raise ValueError("Job URL is required")

    parsed = urlparse(url if "://" in url else f"https://{url}")
    normalized = parsed.geturl()

    if match := _LINKEDIN_PATTERN.search(normalized):
        return JobLinkSite.LINKEDIN, match.group(1)

    if match := _INDEED_PATTERN.search(normalized):
        return JobLinkSite.INDEED, match.group(1)

    if _ZIP_RECRUITER_PATTERN.search(normalized):
        return JobLinkSite.ZIP_RECRUITER, normalized

    raise ValueError(
        "Unsupported job URL. Supported sites: LinkedIn, Indeed, ZipRecruiter"
    )


def _job_post_to_dataframe(job: JobPost, site: str) -> pd.DataFrame:
    job_data = job.dict()
    job_data["site"] = site
    job_data["company"] = job_data["company_name"]
    job_data["job_type"] = (
        ", ".join(job_type.value[0] for job_type in job_data["job_type"])
        if job_data["job_type"]
        else None
    )
    job_data["emails"] = (
        ", ".join(job_data["emails"]) if job_data["emails"] else None
    )
    if job_data["location"]:
        job_data["location"] = Location(**job_data["location"]).display_location()

    job_df = pd.DataFrame([job_data])
    for column in desired_order:
        if column not in job_df.columns:
            job_df[column] = None
    return job_df[desired_order]


def _parse_linkedin_location(location_string: str) -> Location:
    location = Location(country=Country.WORLDWIDE)
    parts = [part.strip() for part in location_string.split(",") if part.strip()]
    if len(parts) == 2:
        location = Location(city=parts[0], state=parts[1], country=Country.WORLDWIDE)
    elif len(parts) >= 3:
        location = Location(
            city=parts[0],
            state=parts[1],
            country=Country.from_string(parts[2]),
        )
    return location


def _fetch_linkedin_job(job_id: str) -> JobPost:
    scraper = LinkedIn()
    scraper.scraper_input = ScraperInput(
        site_type=[Site.LINKEDIN],
        results_wanted=1,
        linkedin_fetch_description=True,
        description_format=DescriptionFormat.MARKDOWN,
    )

    job_url = f"{scraper.base_url}/jobs/view/{job_id}"
    response = scraper.session.get(job_url, timeout=10)
    if response.status_code != 200 or "linkedin.com/signup" in response.url:
        raise ValueError(f"Could not load LinkedIn job page: {job_url}")

    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("h1", class_=lambda c: c and "topcard__title" in c)
    company_tag = soup.find("a", class_="topcard__org-name-link")
    location_tag = soup.find(
        "span", class_=lambda c: c and "topcard__flavor--bullet" in c
    )

    title = title_tag.get_text(strip=True) if title_tag else "N/A"
    company = company_tag.get_text(strip=True) if company_tag else "N/A"
    company_url = company_tag.get("href", "") if company_tag else ""
    location_string = location_tag.get_text(strip=True) if location_tag else "N/A"
    location = _parse_linkedin_location(location_string)

    details = scraper._get_job_details(job_id)
    description = details.get("description")
    if not description and not title_tag:
        raise ValueError(f"Could not parse LinkedIn job details: {job_url}")

    return JobPost(
        id=f"li-{job_id}",
        title=title,
        company_name=company,
        company_url=company_url,
        location=location,
        is_remote=is_job_remote(title, description, location),
        job_url=job_url,
        job_type=details.get("job_type"),
        job_level=(details.get("job_level") or "").lower() or None,
        company_industry=details.get("company_industry"),
        description=description,
        job_url_direct=details.get("job_url_direct"),
        emails=extract_emails_from_text(description) if description else None,
        company_logo=details.get("company_logo"),
        job_function=details.get("job_function"),
    )


def _fetch_indeed_job(job_key: str, source_url: str) -> JobPost:
    import json

    from jobspy.indeed import Indeed
    from jobspy.indeed.util import is_job_remote as indeed_is_remote
    from jobspy.util import markdown_converter

    parsed = urlparse(source_url if "://" in source_url else f"https://{source_url}")
    domain = parsed.netloc or "www.indeed.com"
    base_url = f"https://{domain}"
    country = Country.from_string(domain.split(".")[0])

    scraper = Indeed()
    scraper.scraper_input = ScraperInput(
        site_type=[Site.INDEED],
        country=country,
        results_wanted=1,
        description_format=DescriptionFormat.MARKDOWN,
    )
    scraper.base_url = base_url

    response = scraper.session.get(
        f"{base_url}/viewjob",
        params={"jk": job_key},
        verify=False,
    )
    if response.status_code != 200:
        raise ValueError(
            "Could not load Indeed job page. Try fetching via search instead."
        )

    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find("h1") and "denied" in soup.find("h1").get_text(strip=True).lower():
        raise ValueError(
            "Indeed blocked the request. Try fetching via search instead."
        )

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
        except (TypeError, ValueError):
            continue
        if data.get("@type") != "JobPosting":
            continue

        description_html = data.get("description", "")
        description = (
            markdown_converter(description_html)
            if description_html
            else None
        )
        hiring_org = data.get("hiringOrganization", {})
        location_data = data.get("jobLocation", {})
        if isinstance(location_data, list):
            location_data = location_data[0] if location_data else {}
        address = location_data.get("address", {}) if isinstance(location_data, dict) else {}

        return JobPost(
            id=f"in-{job_key}",
            title=data.get("title", "N/A"),
            company_name=hiring_org.get("name", "Unknown"),
            company_url=hiring_org.get("sameAs"),
            location=Location(
                city=address.get("addressLocality"),
                state=address.get("addressRegion"),
                country=address.get("addressCountry"),
            ),
            description=description,
            job_url=f"{base_url}/viewjob?jk={job_key}",
            is_remote=indeed_is_remote({}, description),
            emails=extract_emails_from_text(description) if description else None,
        )

    raise ValueError(
        "Could not parse Indeed job page. Try fetching via search instead."
    )


def _fetch_ziprecruiter_job(job_url: str) -> JobPost:
    scraper = ZipRecruiter()
    scraper.scraper_input = ScraperInput(
        site_type=[Site.ZIP_RECRUITER],
        results_wanted=1,
        description_format=DescriptionFormat.MARKDOWN,
    )

    response = scraper.session.get(job_url, allow_redirects=True)
    if response.status_code not in range(200, 400):
        raise ValueError(f"Could not load ZipRecruiter job page: {job_url}")

    final_url = response.url
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    company_tag = soup.find("a", class_=lambda c: c and "company_name" in " ".join(c))
    if not company_tag:
        company_tag = soup.find("span", class_=lambda c: c and "hiring_company" in " ".join(c))
    company = company_tag.get_text(strip=True) if company_tag else "Unknown"

    description, job_url_direct = scraper._get_descr(final_url)
    if not description and title == "N/A":
        raise ValueError(f"Could not parse ZipRecruiter job page: {final_url}")

    return JobPost(
        id=f"zr-{urlparse(final_url).path.rstrip('/').split('/')[-1]}",
        title=title,
        company_name=company,
        location=Location(country=Country.USA),
        description=description,
        job_url=final_url,
        job_url_direct=job_url_direct,
        emails=extract_emails_from_text(description) if description else None,
    )


class JobLinkFetcher:
    def fetch_job_by_url(self, url: str) -> pd.DataFrame:
        site, identifier = parse_job_url(url)

        if site == JobLinkSite.LINKEDIN:
            job = _fetch_linkedin_job(identifier)
        elif site == JobLinkSite.INDEED:
            job = _fetch_indeed_job(identifier, url)
        else:
            job = _fetch_ziprecruiter_job(identifier)

        return _job_post_to_dataframe(job, site.value)


job_link_fetcher = JobLinkFetcher()
