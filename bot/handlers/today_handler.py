from datetime import date

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

# ==========================
# SERVICES
# ==========================

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

# ==========================
# /today
# ==========================

async def today(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    summary = (
        report_service
        .get_today_summary()
    )

    message = (
        "📅 Today Summary\n"
        f"{date.today()}\n\n"

        f"💸 Expense\n"
        f"{MoneyHelper.format_rupiah(summary['expense'])}\n\n"

        f"💵 Income\n"
        f"{MoneyHelper.format_rupiah(summary['income'])}\n\n"

        f"💰 Net\n"
        f"{MoneyHelper.format_rupiah(summary['net'])}"
    )

    if summary["categories"]:

        message += (
            "\n\n📊 Top Categories\n"
        )

        sorted_categories = sorted(
            summary[
                "categories"
            ].items(),
            key=lambda x: x[1],
            reverse=True
        )

        for name, amount in (
            sorted_categories[:5]
        ):

            message += (
                f"{name}"
                f" : "
                f"{MoneyHelper.format_rupiah(amount)}\n"
            )

    await (
        update
        .message
        .reply_text(
            message
        )
    )