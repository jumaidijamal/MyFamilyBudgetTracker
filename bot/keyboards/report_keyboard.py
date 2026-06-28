from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton


def report_keyboard():

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(
                    #"📅 Today",
                    "🔥 TODAY TEST 🔥",
                    callback_data="report_today"
                ),

                InlineKeyboardButton(
                    "📆 Week",
                    callback_data="report_week"
                )

            ],

            [

                InlineKeyboardButton(
                    "🗓 Month",
                    callback_data="report_month"
                ),

                InlineKeyboardButton(
                    "📜 History",
                    callback_data="report_history"
                )

            ],

            [

                InlineKeyboardButton(
                    "📊 Summary",
                    callback_data="report_summary"
                )

            ],

            [

                InlineKeyboardButton(
                    "⬅️ Back",
                    callback_data="back_home"
                )

            ]

        ]

    )