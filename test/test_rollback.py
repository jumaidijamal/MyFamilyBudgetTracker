from config import (
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

from services.sheet_service import (
    SheetService
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

trx = (
    transaction_service
    .get_transaction(
        "TRX202606160005"
    )
)

print(
    "Before :",
    balance_service.get_balance(
        trx["Data"]["WalletID"]
    )
)

new_balance = (
    transaction_service
    .rollback_transaction(
        trx["Data"]
    )
)

print(
    "After :",
    new_balance
)