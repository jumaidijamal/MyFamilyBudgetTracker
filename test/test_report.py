from config import *
from services.sheet_service import SheetService
from services.report_service import ReportService

sheet_service = SheetService(
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

report_service = ReportService(
    sheet_service
)

rows = (
    report_service
    .get_all_transactions()
)

for row in rows:

    print(
        row[
            "TransactionDate"
        ],
        type(
            row[
                "TransactionDate"
            ]
        )
    )