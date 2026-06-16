from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Transaction:
    transaction_id: str
    trx_date: date
    created_date: datetime

    user_id: str
    user_name: str

    trx_type: str

    category_id: str
    category_name: str

    wallet_id: str
    wallet_name: str

    amount: float
    description: str

    status: str = "Posted"