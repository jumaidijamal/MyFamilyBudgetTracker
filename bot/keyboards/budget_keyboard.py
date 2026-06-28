from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def budget_keyboard():

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    "💵 Set Budget",

                    callback_data="budget_set"

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