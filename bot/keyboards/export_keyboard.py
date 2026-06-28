from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def export_keyboard():

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(
                    "📄 CSV",
                    callback_data="export_csv"
                ),

                InlineKeyboardButton(
                    "📗 Excel",
                    callback_data="export_excel"
                )

            ],

            [

                InlineKeyboardButton(
                    "📕 PDF",
                    callback_data="export_pdf"
                )

            ],

            [

                InlineKeyboardButton(
                    "⬅️ Back",
                    callback_data="menu_admin"
                )

            ]

        ]

    )