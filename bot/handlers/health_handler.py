from telegram import Update
from telegram.ext import ContextTypes

from config import (
    SPREADSHEET_ID
)

from services.sheet_service import (
    SheetService
)

from services.health_service import (
    HealthService
)

sheet_service = (
    SheetService(
        SPREADSHEET_ID
    )
)

health_service = (
    HealthService(
        sheet_service
    )
)

async def health(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = (
        health_service
        .get_health()
    )

    message = f"""
🟢 Budget Tracker Bot

Bot Status
{data['status']}

Users
{data['users']}

Wallets
{data['wallets']}

Categories
{data['categories']}

Transactions
{data['transactions']}

Server Time
{data['server_time']}
"""

    await (
        update
        .message
        .reply_text(
            message
        )
    )