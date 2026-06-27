from telegram import Update
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes
)

from bot.keyboards.report_keyboard import report_keyboard
from bot.keyboards.admin_keyboard import admin_keyboard


async def home_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "menu_report":

        await query.edit_message_text(
            text="📈 Report Menu",
            reply_markup=report_keyboard()
        )

    elif data == "menu_admin":

        await query.edit_message_text(
            text="⚙️ Admin Menu",
            reply_markup=admin_keyboard()
        )


handler = CallbackQueryHandler(home_callback)