
import datetime
from sheets import SheetsHandler
from sources import naukri, indeed
from config import KEYWORDS, SOURCES

def is_recent(job_date_str):
    return True  # Placeholder for logic

def job_matches_keywords(job, keywords):
    title = job.get("title", "").lower()
    return any(kw.lower() in title for kw in keywords)

def main():
    all_jobs = []
    if "naukri" in SOURCES:
        all_jobs += naukri.scrape()
    if "indeed" in SOURCES:
        all_jobs += indeed.scrape()
    filtered = [job for job in all_jobs if job_matches_keywords(job, KEYWORDS) and is_recent(job.get("date"))]
    sheet = SheetsHandler()
    sheet.append_jobs(filtered)
    print(f"Appended {len(filtered)} jobs.")

if __name__ == "__main__":
    main()
