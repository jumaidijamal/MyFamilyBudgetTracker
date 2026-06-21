from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

from config import (
    DASHBOARD_URL
)

router = Router()


@router.message(
    Command("dashboard")
)
async def dashboard(
    message: Message
):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📊 Open Dashboard",
                    web_app=WebAppInfo(
                        url=DASHBOARD_URL
                    )
                )
            ]
        ]
    )

    await message.answer(
        (
            "📊 <b>Budget Tracker Dashboard</b>\n\n"
            "Buka dashboard interaktif untuk melihat:\n"
            "• Summary Keuangan\n"
            "• Cashflow Trend\n"
            "• Budget Progress\n"
            "• Wallet Balance\n"
            "• Riwayat Transaksi\n"
            "• Analitik Pengeluaran"
        ),
        parse_mode="HTML",
        reply_markup=keyboard
    )