from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def wallet_keyboard():

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "💰 Balance",

                    callback_data="wallet_balance"

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