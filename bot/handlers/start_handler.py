from bot.keyboards.home_keyboard import home_keyboard

async def start(update, context):

    text = """

💰 <b>My Family Budget Tracker</b>

Family Finance Platform

━━━━━━━━━━━━━━━

Selamat datang.

Silakan pilih menu di bawah.

"""

    await update.message.reply_text(

        text,

        parse_mode="HTML",

        reply_markup=home_keyboard()

    )