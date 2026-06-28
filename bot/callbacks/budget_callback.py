from bot.keyboards.budget_keyboard import budget_keyboard
from bot.keyboards.home_keyboard import home_keyboard


async def budget_callback(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data


    if data == "menu_budget":

        await query.edit_message_text(

            "💵 Budget Center",

            reply_markup=budget_keyboard()

        )

        return


    if data == "budget_set":

        await query.edit_message_text(

            "Gunakan command:\n\n"
            "/setbudget kategori nominal"

        )

        return


    if data == "back_home":

        await query.edit_message_text(

            "💰 My Family Budget Tracker",

            reply_markup=home_keyboard()

        )