import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.glassdoor.co.in/Job/india-database-developer-jobs-SRCH_IL.0,5_IN115_KO6,25.htm"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")

    jobs = []
    for div in soup.select(".react-job-listing"):
        title_el = div.select_one("a.jobLink")
        company_el = div.select_one(".job-search-1bgdn7s")
        link = "https://www.glassdoor.co.in" + title_el["href"] if title_el else "#"

        jobs.append({
            "title": title_el.get_text(strip=True) if title_el else "N/A",
            "company": company_el.get_text(strip=True) if company_el else "N/A",
            "location": "India",
            "source": "Glassdoor",
            "date": "Unknown",
            "link": link
        })
    return jobs
