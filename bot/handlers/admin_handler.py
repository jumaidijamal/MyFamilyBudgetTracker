from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

from config import (
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

from services.sheet_service import (
    SheetService
)

from services.admin_service import (
    AdminService
)

BOT_STARTED_AT = (
    datetime.now()
)

sheet_service = (
    SheetService(
        CREDENTIAL_FILE,
        SPREADSHEET_ID
    )
)

admin_service = (
    AdminService(
        sheet_service,
        BOT_STARTED_AT
    )
)


async def admin(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = (
        admin_service
        .get_dashboard()
    )

    message = f"""
👤 Admin Panel

🤖 Bot Status
{data['status']}

👥 Users
{data['users']}

💳 Wallets
{data['wallets']}

📂 Categories
{data['categories']}

🧾 Transactions
{data['transactions']}

🕒 Uptime
{data['uptime']}

🖥 Server Time
{data['server_time']}

📦 Version
{data['version']}
"""

    await (
        update
        .message
        .reply_text(
            message
        )
    )