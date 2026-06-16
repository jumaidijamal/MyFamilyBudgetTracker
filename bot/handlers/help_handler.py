from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = """
💰 Budget Tracker Bot
Personal Finance Platform

━━━━━━━━━━━━━━━
📌 GENERAL
━━━━━━━━━━━━━━━

/start
Memulai bot.

/help
Menampilkan bantuan.

/health
Melihat status bot.

━━━━━━━━━━━━━━━
💸 TRANSACTION
━━━━━━━━━━━━━━━

/lapor
Menambah transaksi baru.

/edit
Mengubah transaksi.

/history
Melihat riwayat transaksi.

/summary
Melihat ringkasan transaksi.

━━━━━━━━━━━━━━━
📊 REPORT
━━━━━━━━━━━━━━━

/today
Laporan hari ini.

/week
Laporan minggu ini.

/month
Laporan bulan ini.

/balance
Melihat saldo seluruh wallet.

━━━━━━━━━━━━━━━
💰 BUDGET
━━━━━━━━━━━━━━━

/setbudget
Membuat atau mengubah budget.

/budget
Melihat penggunaan budget.

━━━━━━━━━━━━━━━
📁 EXPORT
━━━━━━━━━━━━━━━

/export month
Export CSV bulan ini.

/export month xlsx
Export XLSX bulan ini.

━━━━━━━━━━━━━━━
🛠 ADMIN
━━━━━━━━━━━━━━━

/admin
Informasi administrator.

━━━━━━━━━━━━━━━
Version : Project#11
Status : Online 🚀
"""

    await (
        update
        .message
        .reply_text(
            message
        )
    )