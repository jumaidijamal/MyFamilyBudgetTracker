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

from services.wallet_service import (
    WalletService
)

from utils.money_helper import (
    MoneyHelper
)


sheet_service = (
    SheetService(
        SPREADSHEET_ID
    )
)

wallet_service = (
    WalletService(
        sheet_service
    )
)


async def balance(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    wallets = (
        wallet_service
        .get_all_wallets()
    )

    message = (
        "💰 Wallet Balance\n\n"
    )

    current_owner = ""

    total = 0

    for wallet in wallets:

        owner = (
            wallet[
                "Owner"
            ]
        )

        balance = float(
            wallet[
                "CurrentBalance"
            ]
        )

        total += balance

        if (
            owner
            != current_owner
        ):

            current_owner = owner

            if (
                owner
                == "Family"
            ):

                message += (
                    "👨‍👩‍👧 Family\n"
                )

            else:

                message += (
                    f"👤 {owner}\n"
                )

        icon = "🏦"

        if (
            wallet[
                "WalletName"
            ]
            .lower()
            == "cash"
        ):
            icon = "💵"

        message += (
            f"{icon} "
            f"{wallet['WalletName']}\n"
            f"{MoneyHelper.format_rupiah(balance)}\n\n"
        )

    message += (
        "━━━━━━━━━━━━━━\n"
        "💰 Total Asset\n"
        f"{MoneyHelper.format_rupiah(total)}"
    )

    if update.callback_query:

        await update.callback_query.edit_message_text(
            message
        )

    else:

        await update.message.reply_text(
            message
        )