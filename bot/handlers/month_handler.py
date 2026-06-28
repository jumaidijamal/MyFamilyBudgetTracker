from telegram import Update
from telegram.ext import (
    ContextTypes
)

from config import (
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
        SPREADSHEET_ID
    )
)

report_service = (
    ReportService(
        sheet_service
    )
)


async def month(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    summary = (
        report_service
        .get_month_summary()
    )

    month_names = {

        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    month_name = (
        month_names[
            summary[
                "month"
            ]
        ]
    )

    message = f"""
📅 {month_name} {summary['year']}

💸 Expense
{MoneyHelper.format_rupiah(summary['expense'])}

💵 Income
{MoneyHelper.format_rupiah(summary['income'])}

🏦 Saving
{MoneyHelper.format_rupiah(summary['saving'])}

💰 Net
{MoneyHelper.format_rupiah(summary['net'])}
"""

    if (
        summary[
            "categories"
        ]
    ):

        message += (
            "\n📊 Top Categories\n"
        )

        sorted_categories = sorted(
            summary[
                "categories"
            ].items(),
            key=lambda x: x[1],
            reverse=True
        )

        for (
            name,
            amount
        ) in (
            sorted_categories[:5]
        ):

            message += (
                f"\n{name}"
                f" : "
                f"{MoneyHelper.format_rupiah(amount)}"
            )

    if update.callback_query:

        await update.callback_query.edit_message_text(
            message
        )

    else:

        await update.message.reply_text(
            message
        )