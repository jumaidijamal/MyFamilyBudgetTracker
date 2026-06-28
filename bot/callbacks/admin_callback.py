from bot.keyboards.admin_keyboard import admin_keyboard
from bot.keyboards.home_keyboard import home_keyboard

from bot.handlers.health_handler import health
from bot.handlers.admin_handler import admin


async def admin_callback(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data


    if data == "menu_admin":

        await query.edit_message_text(

            "⚙️ Admin Center",

            reply_markup=admin_keyboard()

        )

        return


    if data == "admin_health":

        update.message = query.message
        await health(update, context)
        return


    if data == "admin_panel":

        update.message = query.message
        await admin(update, context)
        return


    if data == "back_home":

        await query.edit_message_text(

            "💰 My Family Budget Tracker",

            reply_markup=home_keyboard()

        )