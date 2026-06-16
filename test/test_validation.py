from config import *
from services.sheet_service import (
    SheetService
)
from services.wallet_service import (
    WalletService
)
from services.category_service import (
    CategoryService
)
from services.validation_service import (
    ValidationService
)

sheet_service = SheetService(
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

wallet_service = WalletService(
    sheet_service
)

category_service = (
    CategoryService(
        sheet_service
    )
)

validation_service = (
    ValidationService(
        wallet_service,
        category_service
    )
)

trx = {
    "type": "expense",
    "amount": 25000,
    "category": "makan",
    "wallet": "bca",
    "description": "nasi goreng"
}

try:

    result = (
        validation_service
        .validate(
            trx
        )
    )

    print(
        "VALIDATION SUCCESS"
    )

    print(result)

except Exception as e:

    print(e)