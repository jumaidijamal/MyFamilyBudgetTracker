from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def help_keyboard():

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(
                    "📖 User Guide",
                    callback_data="help_guide"
                ),

                InlineKeyboardButton(
                    "❓ FAQ",
                    callback_data="help_faq"
                )

            ],

            [

                InlineKeyboardButton(
                    "🌐 Dashboard Guide",
                    callback_data="help_dashboard"
                ),

                InlineKeyboardButton(
                    "💰 Budget Guide",
                    callback_data="help_budget"
                )

            ],

            [

                InlineKeyboardButton(
                    "❤️ About",
                    callback_data="help_about"
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