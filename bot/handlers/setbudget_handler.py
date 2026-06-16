from telegram import Update
from telegram.ext import ContextTypes

from config import (
    SPREADSHEET_ID
)

from services.sheet_service import (
    SheetService
)

from services.user_service import (
    UserService
)

from services.category_service import (
    CategoryService
)

from services.budget_service import (
    BudgetService
)

sheet_service = (
    SheetService(
        SPREADSHEET_ID
    )
)

user_service = (
    UserService(
        sheet_service
    )
)

category_service = (
    CategoryService(
        sheet_service
    )
)

budget_service = (
    BudgetService(
        sheet_service
    )
)

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

async def setbudget(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    
    if len(
        context.args
    ) != 2:

        await (
            update
            .message
            .reply_text(
                "📌 Format:\n\n"
                "/setbudget "
                "<category> "
                "<amount>\n\n"
                "Contoh:\n"
                "/setbudget "
                "makan "
                "1000000"
            )
        )

        return
    
    category_name = (
        context.args[0]
        .lower()
    )

    amount = float(
        context.args[1]
    )

    try:

        amount = float(
            context.args[1]
        )

    except:

        await (
            update
            .message
            .reply_text(
                "❌ Amount harus angka."
            )
        )

        return
    
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
                "❌ User belum terdaftar."
            )
        )

        return
    
    category = (
    category_service
        .get_category(
            category_name
        )
    )

    if category is None:

        await (
            update
            .message
            .reply_text(
                "❌ Category tidak ditemukan."
            )
        )

        return
    
    budget = (
        budget_service
        .get_budget(
            user[
                "UserID"
            ],
            category[
                "CategoryID"
            ]
        )
    )

    if budget is None:

        result = (
            budget_service
            .create_budget(
                user,
                category,
                amount
            )
        )

        message = f"""
    ✅ Budget Created

    Category :
    {category['CategoryName']}

    Budget :
    {format_rupiah(amount)}

    Period :
    Monthly
    """

        await (
            update
            .message
            .reply_text(
                message
            )
        )

        return
    
    old_amount = (
        budget[
            "Amount"
        ]
    )

    budget_service.update_budget(
        budget[
            "BudgetID"
        ],
        amount
    )

    message = f"""
    ✅ Budget Updated

    Category :
    {category['CategoryName']}

    Old Budget :
    {format_rupiah(old_amount)}

    New Budget :
    {format_rupiah(amount)}
    """

    await (
        update
        .message
        .reply_text(
            message
        )
    )