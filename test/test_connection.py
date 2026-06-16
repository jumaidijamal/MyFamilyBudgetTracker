from dotenv import load_dotenv
import os
import json

from services.sheet_service import SheetService
from config import CREDENTIAL_FILE

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

print("Spreadsheet ID:", SPREADSHEET_ID)
print("Credential File:", CREDENTIAL_FILE)

with open(CREDENTIAL_FILE, encoding="utf-8") as f:
    data = json.load(f)

print("Client Email:", data["client_email"])
print("Project ID:", data["project_id"])

sheet_service = SheetService(
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

sheet = sheet_service.get_sheet("Wallets")

rows = sheet.get_all_records()

for row in rows:
    print(row)