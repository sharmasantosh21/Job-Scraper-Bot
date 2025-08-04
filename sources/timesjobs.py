import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=sql+developer&txtLocation="
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")

    jobs = []
    for div in soup.select(".job-bx"):
        title_el = div.select_one("h2 a")
        company_el = div.select_one(".comp-name")
        location_el = div.select_one(".loc")
        link = title_el["href"]

        jobs.append({
            "title": title_el.get_text(strip=True),
            "company": company_el.get_text(strip=True) if company_el else "N/A",
            "location": location_el.get_text(strip=True) if location_el else "N/A",
            "source": "TimesJobs",
            "date": "Unknown",
            "link": link
        })
    return jobs
