import json
import os
import gspread
from google.oauth2.service_account import (
    Credentials
)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


class SheetService:

    def __init__(
        self,
        spreadsheet_id
    ):

        if not spreadsheet_id:
            raise ValueError(
                "SPREADSHEET_ID environment variable not found."
            )

        google_credentials = os.getenv(
            "GOOGLE_CREDENTIALS"
        )

        if google_credentials:

            try:

                credentials_info = json.loads(
                    google_credentials
                )

            except json.JSONDecodeError:

                raise ValueError(
                    "Invalid GOOGLE_CREDENTIALS JSON."
                )

            creds = (
                Credentials
                .from_service_account_info(
                    credentials_info,
                    scopes=SCOPES
                )
            )

        else:

            credential_file = (
                "credentials/service_account.json"
            )

            if not os.path.exists(
                credential_file
            ):
                raise FileNotFoundError(
                    f"{credential_file} not found."
                )

            creds = (
                Credentials
                .from_service_account_file(
                    credential_file,
                    scopes=SCOPES
                )
            )

        self.client = (
            gspread.authorize(
                creds
            )
        )

        self.spreadsheet = (
            self.client.open_by_key(
                spreadsheet_id
            )
        )

    def get_sheet(
        self,
        sheet_name
    ):
        return (
            self.spreadsheet
            .worksheet(
                sheet_name
            )
        )

    def get_all_records(
        self,
        sheet_name
    ):
        worksheet = (
            self.get_sheet(
                sheet_name
            )
        )

        return (
            worksheet
            .get_all_records()
        )