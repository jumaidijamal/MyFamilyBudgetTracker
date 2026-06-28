from telegram.ext import CallbackQueryHandler

from bot.callbacks.report_callback import report_callback
from bot.callbacks.wallet_callback import wallet_callback
from bot.callbacks.budget_callback import budget_callback
from bot.callbacks.admin_callback import admin_callback
from bot.callbacks.help_callback import help_callback

from bot.keyboards.home_keyboard import home_keyboard


async def home_callback(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "menu_report":

        await report_callback(update, context)
        return

    if data == "menu_wallet":

        await wallet_callback(update, context)
        return

    if data == "menu_budget":

        await budget_callback(update, context)
        return

    if data == "menu_admin":

        await admin_callback(update, context)
        return

    if data == "menu_help":

        await help_callback(update, context)
        return


    if data == "back_home":

        await query.edit_message_text(

            "💰 My Family Budget Tracker\n\n"
            "Silakan pilih menu.",

            reply_markup=home_keyboard()

        )


handler = CallbackQueryHandler(home_callback)