import json
import os
import gspread  
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


class SheetService:

    def __init__(
        self,
        credential_file,
        spreadsheet_id
    ):

        credentials_info = json.loads(
            os.getenv("GOOGLE_CREDENTIALS")
        )

        creds = Credentials.from_service_account_info(
            credentials_info,
            scopes=SCOPES
        )

        #creds = Credentials.from_service_account_file(
        #    credential_file,
        #    scopes=SCOPES
        #)

        self.client = gspread.authorize(creds)
        self.spreadsheet = (
            self.client.open_by_key(
                spreadsheet_id
            )
        )

    def get_sheet(self, sheet_name):
        return self.spreadsheet.worksheet(
            sheet_name
        )
