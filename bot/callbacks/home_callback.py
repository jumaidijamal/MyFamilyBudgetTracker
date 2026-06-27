from telegram import Update

from telegram.ext import ContextTypes

from telegram.ext import CallbackQueryHandler


async def home_callback(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    query = update.callback_query

    await query.answer()

    await query.message.reply_text(

        f"Menu : {query.data}"

    )


handler = CallbackQueryHandler(

    home_callback

)