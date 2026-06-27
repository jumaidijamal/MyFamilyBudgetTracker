from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

from config import DASHBOARD_URL


def get_home_keyboard():

    return InlineKeyboardMarkup(

        [

            [
                InlineKeyboardButton(
                    text="📊 Dashboard",
                    web_app=WebAppInfo(DASHBOARD_URL)
                )
            ],

            [
                InlineKeyboardButton(
                    text="💰 Balance",
                    callback_data="balance"
                ),

                InlineKeyboardButton(
                    text="📅 Today",
                    callback_data="today"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📆 Week",
                    callback_data="week"
                ),

                InlineKeyboardButton(
                    text="🗓 Month",
                    callback_data="month"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📜 History",
                    callback_data="history"
                ),

                InlineKeyboardButton(
                    text="📊 Summary",
                    callback_data="summary"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💵 Budget",
                    callback_data="budget"
                ),

                InlineKeyboardButton(
                    text="📤 Export",
                    callback_data="export"
                )
            ],

            [
                InlineKeyboardButton(
                    text="❤️ Health",
                    callback_data="health"
                ),

                InlineKeyboardButton(
                    text="❓ Help",
                    callback_data="help"
                )
            ]
        ]
    )