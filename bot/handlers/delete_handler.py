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

from services.balance_service import (
    BalanceService
)

from services.transaction_service import (
    TransactionService
)

sheet_service = (
    SheetService(
        CREDENTIAL_FILE,
        SPREADSHEET_ID
    )
)

balance_service = (
    BalanceService(
        sheet_service
    )
)

transaction_service = (
    TransactionService(
        sheet_service,
        balance_service
    )
)


async def delete(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if (
        len(
            context.args
        )
        != 1
    ):

        await (
            update
            .message
            .reply_text(
                "Usage:\n/delete TRX202606160003"
            )
        )

        return

    trx_id = (
        context.args[0]
        .strip()
    )

    try:

        result = (
            transaction_service
            .delete_transaction(
                trx_id
            )
        )

        await (
            update
            .message
            .reply_text(
                f"""
🗑 Transaction Deleted

ID:
{result['TransactionID']}

New Balance:
Rp{result['NewBalance']:,.0f}
"""
            )
        )

    except Exception as e:

        await (
            update
            .message
            .reply_text(
                f"❌ {str(e)}"
            )
        )