from datetime import date

from config import (
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

from services.sheet_service import SheetService
from services.wallet_service import WalletService
from services.category_service import CategoryService
from services.balance_service import BalanceService
from services.transaction_service import TransactionService


sheet_service = SheetService(
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

wallet_service = WalletService(
    sheet_service
)

category_service = CategoryService(
    sheet_service
)

balance_service = BalanceService(
    sheet_service
)

transaction_service = TransactionService(
    sheet_service,
    balance_service
)

wallet = (
    wallet_service
    .get_wallet(
        "bca"
    )
)

category = (
    category_service
    .get_category(
        "makan"
    )
)

trx = {
    "date": date.today(),
    "type": "expense",
    "amount": 25000,
    "category": "makan",
    "wallet": "bca",
    "description": "nasi goreng"
}

user = {
    "UserID": "U001",
    "DisplayName": "Jumaidi"
}

result = (
    transaction_service
    .save_transaction(
        trx,
        user,
        wallet,
        category
    )
)

print(result)