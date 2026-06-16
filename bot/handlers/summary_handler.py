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


async def summary(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    data = (
        report_service
        .get_asset_summary()
    )

    owners = (
        data[
            "Owners"
        ]
    )

    total_assets = (
        data[
            "TotalAssets"
        ]
    )

    message = ""

    owner_titles = {

        "Jumaidi":
            "👨 Jumaidi",

        "Tika":
            "👩 Tika",

        "Family":
            "👨‍👩‍👧 Shared"
    }

    for owner, wallets in (
        owners.items()
    ):

        message += (
            f"{owner_titles.get(owner, owner)}\n\n"
        )

        owner_total = 0

        for wallet in wallets:

            icon = (
                "🏦"
            )

            if (
                wallet[
                    "WalletName"
                ]
                .lower()
                == "cash"
            ):
                icon = "💵"

            balance = (
                wallet[
                    "Balance"
                ]
            )

            owner_total += balance

            message += (
                f"{icon} "
                f"{wallet['WalletName']}\n"
                f"{MoneyHelper.format_rupiah(balance)}\n\n"
            )

        message += (
            f"Subtotal : "
            f"{MoneyHelper.format_rupiah(owner_total)}\n"
            f"\n━━━━━━━━━━\n\n"
        )

    message += (
        f"💰 Total Assets\n"
        f"{MoneyHelper.format_rupiah(total_assets)}"
    )

    await (
        update
        .message
        .reply_text(
            message
        )
    )