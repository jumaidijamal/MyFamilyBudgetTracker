from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.home_keyboard import (
    get_home_keyboard
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = """
💰 <b>My Family Budget Tracker</b>

<i>Family Finance Platform</i>

━━━━━━━━━━━━━━━━━━

Selamat datang 👋

Kelola seluruh keuangan keluarga dalam satu tempat.

✨ Fitur Utama

💸 Catat transaksi

👛 Kelola Wallet

📊 Dashboard Interaktif

💰 Budget Management

📈 Financial Report

📤 Export CSV / Excel

━━━━━━━━━━━━━━━━━━

👇 Pilih menu di bawah.
"""

    await update.message.reply_text(

        text,

        parse_mode="HTML",

        reply_markup=get_home_keyboard()

    )