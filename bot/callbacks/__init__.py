from telegram.ext import CallbackQueryHandler

from bot.callbacks.home_callback import home_callback
from bot.callbacks.report_callback import report_callback
from bot.callbacks.wallet_callback import wallet_callback
from bot.callbacks.budget_callback import budget_callback
from bot.callbacks.admin_callback import admin_callback
from bot.callbacks.help_callback import help_callback
from bot.callbacks.export_callback import export_callback


def register_callbacks(app):

    # HOME MENU ONLY
    app.add_handler(
        CallbackQueryHandler(
            home_callback,
            pattern="^(menu_|back_home$)"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            report_callback,
            pattern="^report_"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            wallet_callback,
            pattern="^wallet_"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            budget_callback,
            pattern="^budget_"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            admin_callback,
            pattern="^(admin_|menu_admin$)"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            help_callback,
            pattern="^help_|^menu_help$"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            export_callback,
            pattern="^(export_|admin_export$)"
        )
    )