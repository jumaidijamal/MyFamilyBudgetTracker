from bot.keyboards.wallet_keyboard import wallet_keyboard
from bot.keyboards.home_keyboard import home_keyboard

from bot.handlers.balance_handler import balance


async def wallet_callback(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data


    if data == "menu_wallet":

        await query.edit_message_text(

            "👛 Wallet Center",

            reply_markup=wallet_keyboard()

        )

        return


    if data == "wallet_balance":

        update.message = query.message
        await balance(update, context)
        return


    if data == "back_home":

        await query.edit_message_text(

            "💰 My Family Budget Tracker",

            reply_markup=home_keyboard()

        )