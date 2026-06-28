from bot.keyboards.home_keyboard import home_keyboard

from bot.handlers.help_handler import help_command


async def help_callback(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data


    if data == "menu_help":

        update.message = query.message

        await help_command(update, context)

        return


    if data == "back_home":

        await query.edit_message_text(

            "💰 My Family Budget Tracker",

            reply_markup=home_keyboard()

        )