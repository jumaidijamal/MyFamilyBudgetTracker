from telegram import Update

from telegram.ext import ContextTypes

from telegram.ext import CallbackQueryHandler


async def home_callback(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "menu_report":

        await query.edit_message_text(

            "📈 Report Menu",

            reply_markup=report_keyboard()

        )

    elif data == "menu_admin":

        await query.edit_message_text(

            "⚙️ Admin",

            reply_markup=admin_keyboard()

        )


handler = CallbackQueryHandler(

    home_callback

)