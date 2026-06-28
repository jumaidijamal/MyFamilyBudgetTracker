from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def admin_keyboard():

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "❤️ Health",

                    callback_data="admin_health"

                ),

                InlineKeyboardButton(

                    "📤 Export",

                    callback_data="admin_export"

                )

            ],

            [

                InlineKeyboardButton(

                    "⚙️ Admin",

                    callback_data="admin_panel"

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