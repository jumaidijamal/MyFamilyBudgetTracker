def admin_keyboard():

    return InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(
                    "📁 Export",
                    callback_data="admin_export"
                )

            ],

            [

                InlineKeyboardButton(
                    "💰 Budget",
                    callback_data="admin_budget"
                )

            ],

            [

                InlineKeyboardButton(
                    "❤️ Health",
                    callback_data="admin_health"
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