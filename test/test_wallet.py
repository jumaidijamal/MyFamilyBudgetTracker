from config import (
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

from services.sheet_service import SheetService
from services.wallet_service import WalletService

sheet_service = SheetService(
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

wallet_service = WalletService(
    sheet_service
)

print(
    wallet_service.get_wallet(
        "bca"
    )
)