
import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.naukri.com/software-database-developer-jobs-in-india?k=database+developer"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    jobs = []
    for div in soup.select(".jobTuple"):
        title_el = div.select_one(".title a")
        company_el = div.select_one(".companyInfo .subTitle")
        location_el = div.select_one(".location span")
        link = title_el["href"]
        jobs.append({
            "title": title_el.get_text(strip=True),
            "company": company_el.get_text(strip=True) if company_el else "",
            "location": location_el.get_text(strip=True) if location_el else "",
            "source": "Naukri",
            "date": "Unknown",
            "link": link
        })
    return jobs
