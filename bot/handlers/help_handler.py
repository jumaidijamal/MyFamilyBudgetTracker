from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = """

📌 Available Commands

/start
/help   
/lapor
/laporanhariini
/laporanmingguini
/laporanbulanini

"""

    await update.message.reply_text(
        message
    )