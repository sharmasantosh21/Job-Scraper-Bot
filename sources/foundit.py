import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.foundit.in/srp/results?query=database%20developer&location=india"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")

    jobs = []
    for div in soup.select(".srp-jobtuple-wrapper"):
        title_el = div.select_one("h3 a")
        company_el = div.select_one(".company-name span")
        location_el = div.select_one(".job-tuple-location span")
        link = title_el["href"]

        jobs.append({
            "title": title_el.get_text(strip=True) if title_el else "N/A",
            "company": company_el.get_text(strip=True) if company_el else "N/A",
            "location": location_el.get_text(strip=True) if location_el else "N/A",
            "source": "Foundit",
            "date": "Unknown",
            "link": link
        })
    return jobs
