from telegram import Update
from telegram.ext import ContextTypes

from config import (
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

from services.sheet_service import SheetService
from services.parser_service import ParserService
from services.wallet_service import WalletService
from services.category_service import CategoryService
from services.balance_service import BalanceService
from services.transaction_service import TransactionService
from services.user_service import UserService


# ==========================
# SERVICES (Singleton Style)
# ==========================

sheet_service = SheetService(
    CREDENTIAL_FILE,
    SPREADSHEET_ID
)

parser_service = ParserService()

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

user_service = UserService(
    sheet_service
)


# ==========================
# HELPER
# ==========================

def format_rupiah(
    amount
):

    return (
        "Rp{:,.0f}"
        .format(amount)
        .replace(
            ",",
            "."
        )
    )


# ==========================
# /edit
# ==========================

async def edit_transaction(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    #print("========== UPDATE CALLED ==========")
    #print(repr(update.message.text))
    
    try:

        text = (
            update
            .message
            .text
        )

        text = (
            text
            .replace(
                "/edit",
                "",
                1
            )
            .strip()
        )

        # ==========================
        # FORMAT HELP
        # ==========================

        if not text:

            await (
                update
                .message
                .reply_text(
                    "📌 Format:\n\n"
                    "/edit TRX_ID\n\n"
                    "expense\n"
                    "25000\n"
                    "makan\n"
                    "bca\n"
                    "nasi goreng"
                )
            )

            return

        # ==========================
        # PARSE
        # ==========================

        try:
            lines = [
                x.strip()
                for x in text.splitlines()
                if x.strip()
            ]

            if len(lines) < 6:

                await update.message.reply_text(
                    "📌 Format:\n\n"
                    "/edit TRX_ID\n\n"
                    "expense\n"
                    "25000\n"
                    "makan\n"
                    "bca\n"
                    "nasi goreng"
                )

                return

            transaction_id = (
                lines[0]
            )

            old = (
                transaction_service
                .get_transaction(
                    transaction_id
                )
            )

            if old is None:

                await update.message.reply_text(
                    "❌ Transaction ID tidak ditemukan."
                )

                return

            trx_text = "\n".join(
                lines[1:]
            )

            trx = (
                parser_service
                .parse_update(
                    trx_text
                )
            )

        except Exception as e:

            await (
                update
                .message
                .reply_text(
                    f"❌ Format salah.\n\n{str(e)}"
                )
            )

            return

        # ==========================
        # GET USER
        # ==========================

        telegram_id = (
            update
            .effective_user
            .id
        )

        user = (
            user_service
            .get_user_by_telegram_id(
                telegram_id
            )
        )

        if user is None:

            await (
                update
                .message
                .reply_text(
                    "❌ Telegram ID Anda belum terdaftar."
                )
            )

            return

        # ==========================
        # GET WALLET
        # ==========================

        wallet = (
            wallet_service
            .get_wallet(
                trx[
                    "wallet"
                ]
            )
        )

        if wallet is None:

            suggestions = (
                wallet_service
                .suggest_wallet(
                    trx[
                        "wallet"
                    ]
                )
            )

            message = (
                "❌ Wallet tidak ditemukan."
            )

            if suggestions:

                message += (
                    "\n\nMungkin maksud Anda:\n"
                )

                for item in suggestions:

                    message += (
                        f"• {item}\n"
                    )

            await (
                update
                .message
                .reply_text(
                    message
                )
            )

            return

        # ==========================
        # GET CATEGORY
        # ==========================

        category = (
            category_service
            .get_category(
                trx[
                    "category"
                ]
            )
        )

        if category is None:

            suggestions = (
                category_service
                .suggest_category(
                    trx[
                        "category"
                    ]
                )
            )

            message = (
                "❌ Category tidak ditemukan."
            )

            if suggestions:

                message += (
                    "\n\nMungkin maksud Anda:\n"
                )

                for item in suggestions:

                    message += (
                        f"• {item}\n"
                    )

            await (
                update
                .message
                .reply_text(
                    message
                )
            )

            return

        # ==========================
        # SAVE TRANSACTION
        # ==========================

        try:

            result = (
                transaction_service
                .edit_transaction(
                    transaction_id,
                    trx,
                    wallet,
                    category
                )
            )

        except Exception as e:

            await (
                update
                .message
                .reply_text(
                    f"❌ Gagal menyimpan transaksi.\n\n{str(e)}"
                )
            )

            return

        # ==========================
        # SUCCESS MESSAGE
        # ==========================

        message = f"""
✅ Transaction Updated

ID : {result['TransactionID']}

Date : {trx['date']}
Type : {trx['type'].title()}
Category : {category['CategoryName']}
Wallet : {wallet['WalletName']}
Amount : {format_rupiah(trx['amount'])}
Description : {trx['description']}

💰 New Balance
{wallet['WalletName']}

{format_rupiah(
    result['NewBalance']
)}
"""

        await (
            update
            .message
            .reply_text(
                message
            )
        )

    except Exception as e:

        await (
            update
            .message
            .reply_text(
                f"❌ Unexpected Error\n\n{str(e)}"
            )
        )