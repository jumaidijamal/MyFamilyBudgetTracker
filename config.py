from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv(
    "BOT_TOKEN"
)

SPREADSHEET_ID = os.getenv(
    "SPREADSHEET_ID"
)

GOOGLE_CREDENTIALS = os.getenv(
    "GOOGLE_CREDENTIALS"
)

INCOME_TYPE = "income"
EXPENSE_TYPE = "expenses"
SAVINGS_TYPE = "savings"