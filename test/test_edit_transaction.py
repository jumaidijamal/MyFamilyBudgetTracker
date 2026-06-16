from datetime import date

from config import (
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

from services.sheet_service import (
    SheetService
)

from services.wallet_service import (
    WalletService
)

from services.category_service import (
    CategoryService
)

from services.balance_service import (
    BalanceService
)

from services.transaction_service import (
    TransactionService
)

sheet_service = (
    SheetService(
        CREDENTIAL_FILE,
        SPREADSHEET_ID
    )
)

wallet_service = (
    WalletService(
        sheet_service
    )
)

category_service = (
    CategoryService(
        sheet_service
    )
)

balance_service = (
    BalanceService(
        sheet_service
    )
)

transaction_service = (
    TransactionService(
        sheet_service,
        balance_service
    )
)

trx = {

    "date":
        date.today(),

    "type":
        "expense",

    "amount":
        50000,

    "category":
        "transport",

    "wallet":
        "mandiri",

    "description":
        "grab pulang"
}

wallet = (
    wallet_service
    .get_wallet(
        "mandiri"
    )
)

category = (
    category_service
    .get_category(
        "transport"
    )
)

result = (
    transaction_service
    .edit_transaction(
        "TRX202606160005",
        trx,
        wallet,
        category
    )
)

print(result)