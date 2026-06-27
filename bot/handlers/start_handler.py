from telegram import Update
from telegram.ext import ContextTypes
from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

from config import DASHBOARD_URL
print(DASHBOARD_URL)

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            text="📊 Dashboard",
            web_app=WebAppInfo(DASHBOARD_URL)
        )
    ]
])

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = """
💰 My Family Budget Tracker Bot
Family Finance Platform

💡 Motto:
"Catat uangmu hari ini, amankan masa depanmu."

Selamat datang!

Bot ini membantu Anda untuk:

💸 Mencatat pengeluaran (Expense)
💵 Mencatat pemasukan (Income)
👛 Memantau saldo setiap wallet
📊 Membuat laporan harian, mingguan, dan bulanan
💰 Mengelola budget per kategori
📁 Export laporan ke CSV dan Excel
☁️ Menyimpan data secara online 24/7

━━━━━━━━━━━━━━━
🚀 Quick Start
━━━━━━━━━━━━━━━

1️⃣ Tambah transaksi

/lapor

expense
25000
makan
bca
nasi goreng

2️⃣ Lihat saldo

/balance

3️⃣ Lihat laporan hari ini

/today

4️⃣ Atur budget

/setbudget makan 1000000

5️⃣ Lihat seluruh command

/help

━━━━━━━━━━━━━━━
📌 Status
━━━━━━━━━━━━━━━

Version : Project#11
Mode : Production
Platform : Railway ☁️
Database : Google Sheets 📊

Selamat mengelola keuangan Anda! 💰🚀
"""

    await (
        update
        .message
        .reply_text(
            #message
            "Selamat datang di Budget Tracker!",
            reply_markup=keyboard
        )
    )