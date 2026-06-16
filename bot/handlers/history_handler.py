from telegram import Update
from telegram.ext import (
    ContextTypes
)

from config import (
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

from services.sheet_service import (
    SheetService
)

from services.report_service import (
    ReportService
)

from utils.money_helper import (
    MoneyHelper
)

sheet_service = (
    SheetService(
        CREDENTIAL_FILE,
        SPREADSHEET_ID
    )
)

report_service = (
    ReportService(
        sheet_service
    )
)


async def history(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    rows = (
        report_service
        .get_recent_transactions()
    )

    if not rows:

        await (
            update
            .message
            .reply_text(
                "📭 Belum ada transaksi."
            )
        )

        return

    #message = (
    #    "🧾 Last Transactions\n\n"
    #)

    message = (
        f"📜 Transaction History\n"
        f"Total : {len(rows)} transaksi\n\n"
    )

    for index, row in enumerate(
        rows,
        start=1
    ):

        status = (
            row["Status"]
            .lower()
        )

        if status == "posted":
            status_icon = "🟢 Posted"
        else:
            status_icon = "🔴 Deleted"
        
        trx_icon = (
            "💸"
            if row["Type"].lower() == "expense"
            else "💵"
        )

        message += (
            f"{index}.\n"
            f"🆔 {row['TransactionID']}\n"
            f"📅 {row['TransactionDate']}\n"
            f"{trx_icon} {row['Type'].title()}\n"
            #f"📌 {row['Type'].title()}\n"
            f"🏷 {row['CategoryName']}\n"
            f"🏦 {row['WalletName']}\n"
            f"💰 {MoneyHelper.format_rupiah(float(row['Amount']))}\n"
            f"📝 {row['Description']}\n"
            f"{status_icon}\n"
            f"\n━━━━━━━━━━\n\n"
        )

    await (
        update
        .message
        .reply_text(
            message
        )
    )