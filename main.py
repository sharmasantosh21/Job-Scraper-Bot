import datetime
from sheets import SheetsHandler
from sources import naukri, indeed, timesjobs, foundit, glassdoor
from config import KEYWORDS, SOURCES

def is_recent(job_date_str):
    return True  # Placeholder for logic

def job_matches_keywords(job, keywords):
    title = job.get("title", "").lower()
    return any(kw.lower() in title for kw in keywords)

def main():
    all_jobs = []

    print("Scraping Naukri...")
    if "naukri" in SOURCES:
        naukri_jobs = naukri.scrape()
        print(f"Found {len(naukri_jobs)} Naukri jobs")
        all_jobs += naukri_jobs

    print("Scraping Indeed...")
    if "indeed" in SOURCES:
        indeed_jobs = indeed.scrape()
        print(f"Found {len(indeed_jobs)} Indeed jobs")
        all_jobs += indeed_jobs

    print("Scraping TimesJobs...")
    if "timesjobs" in SOURCES:
        timesjobs_jobs = timesjobs.scrape()
        print(f"Found {len(timesjobs_jobs)} TimesJobs jobs")
        all_jobs += timesjobs_jobs

    print("Scraping Foundit...")
    if "foundit" in SOURCES:
        foundit_jobs = foundit.scrape()
        print(f"Found {len(foundit_jobs)} Foundit jobs")
        all_jobs += foundit_jobs

    print("Scraping Glassdoor...")
    if "glassdoor" in SOURCES:
        glassdoor_jobs = glassdoor.scrape()
        print(f"Found {len(glassdoor_jobs)} Glassdoor jobs")
        all_jobs += glassdoor_jobs

    # Filter results
    filtered = [job for job in all_jobs if job_matches_keywords(job, KEYWORDS) and is_recent(job.get("date"))]
    print(f"Jobs after filtering: {len(filtered)}")

    # Push to Google Sheets
    sheet = SheetsHandler()
    sheet.append_jobs(filtered)
    print(f"Appended {len(filtered)} jobs to sheet.")

if __name__ == "__main__":
    main()
