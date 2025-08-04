
import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.indeed.co.in/jobs?q=database+developer&l=India"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    jobs = []
    for div in soup.select(".jobsearch-SerpJobCard"):
        title_el = div.select_one(".title a")
        company_el = div.select_one(".sjcl .company")
        location_el = div.select_one(".sjcl .location")
        link = "https://www.indeed.co.in" + title_el["href"]
        jobs.append({
            "title": title_el.get_text(strip=True),
            "company": company_el.get_text(strip=True) if company_el else "",
            "location": location_el.get_text(strip=True) if location_el else "",
            "source": "Indeed",
            "date": "Unknown",
            "link": link
        })
    return jobs
