import os

# ✅ Write credentials.json file from GitHub Actions Secret
if os.environ.get("GOOGLE_CREDENTIALS_JSON"):
    with open("credentials.json", "w") as f:
        f.write(os.environ["GOOGLE_CREDENTIALS_JSON"])


import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GOOGLE_SERVICE_ACCOUNT_FILE, SPREADSHEET_ID, SHEET_NAME

class SheetsHandler:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(
            GOOGLE_SERVICE_ACCOUNT_FILE,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        self.service = build("sheets", "v4", credentials=creds)
        self.sheet = self.service.spreadsheets()

    def append_jobs(self, jobs):
        if not jobs:
            return
        values = []
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        for job in jobs:
            values.append([
                job.get("title"),
                job.get("company"),
                job.get("location", ""),
                job.get("source"),
                job.get("date", today),
                job.get("link")
            ])
        body = {"values": values}
        self.sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:F",
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body=body
        ).execute()
