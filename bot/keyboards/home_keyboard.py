from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)

from config import DASHBOARD_URL


def home_keyboard():

    return InlineKeyboardMarkup(

        [

            [
                InlineKeyboardButton(
                    "📊 Dashboard",
                    web_app=WebAppInfo(DASHBOARD_URL)
                )
            ],

            [

                InlineKeyboardButton(
                    "💰 Report",
                    callback_data="menu_report"
                ),

                InlineKeyboardButton(
                    "💳 Wallet",
                    callback_data="menu_wallet"
                )

            ],

            [

                InlineKeyboardButton(
                    "📈 Budget",
                    callback_data="menu_budget"
                ),

                InlineKeyboardButton(
                    "⚙️ Admin",
                    callback_data="menu_admin"
                )

            ],

            [

                InlineKeyboardButton(
                    "❓ Help",
                    callback_data="menu_help"
                )

            ]

        ]

    )