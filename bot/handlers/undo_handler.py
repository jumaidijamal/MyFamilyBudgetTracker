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

from services.balance_service import (
    BalanceService
)

from services.transaction_service import (
    TransactionService
)

sheet_service = (
    SheetService(
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


async def undo(
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
                "Usage:\n/undo TRX202606160003"
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
            .undo_transaction(
                trx_id
            )
        )

        await (
            update
            .message
            .reply_text(
                f"""
♻️ Transaction Restored

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