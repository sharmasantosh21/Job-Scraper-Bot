# Job Scraper Bot

Scrapes software/database developer jobs in India (posted in last 48h) and updates a Google Sheet.

## Setup

1. Clone this repo.
2. Set up Google Cloud service account, enable Sheets API, download JSON.
3. Copy `credentials_sample.json` to `credentials.json`.
4. Fill in `config.py`.
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Test scraping:
   ```
   python main.py
   ```
7. Configure GitHub Actions for daily run.

## Usage
Outputs into Google Sheet defined in config. Each run appends new jobs.
