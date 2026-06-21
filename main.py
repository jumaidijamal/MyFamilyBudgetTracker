from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN

from bot.handlers.start_handler import start
from bot.handlers.help_handler import help_command
from bot.handlers.update_handler import update_transaction
from bot.handlers.balance_handler import balance
from bot.handlers.today_handler import today
from bot.handlers.week_handler import week
from bot.handlers.month_handler import month
from bot.handlers.history_handler import history
from bot.handlers.summary_handler import summary
from bot.handlers.delete_handler import delete
from bot.handlers.undo_handler import undo
from bot.handlers.edit_handler import edit_transaction
from bot.handlers.health_handler import health
from bot.handlers.admin_handler import admin
from bot.handlers.export_handler import export
from bot.handlers.setbudget_handler import setbudget
from fastapi.templating import (
    Jinja2Templates
)
from fastapi import Request

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from bot.handlers.unknown_handler import (
    unknown
)


templates = Jinja2Templates(
    directory="templates"
)

app = (
    Application
    .builder()
    .token(
        BOT_TOKEN
    )
    .build()
)

@app.get("/dashboard")
async def dashboard_page(
    request: Request
):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request
        }
    )

# ==========================
# /START
# ==========================
app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

# ==========================
# /HELP
# ==========================
app.add_handler(
    CommandHandler(
        "help",
        help_command
    )
)

# ==========================
# /LAPOR
# ==========================
app.add_handler(
    CommandHandler(
        "lapor",
        update_transaction
    )
)

# ==========================
# /BALANCE
# ==========================
app.add_handler(
    CommandHandler(
        "balance",
        balance
    )
)

# ==========================
# /TODAY
# ==========================
app.add_handler(
    CommandHandler(
        "today",
        today
    )
)

# ==========================
# /WEEK
# ==========================
app.add_handler(
    CommandHandler(
        "week",
        week
    )
)

# ==========================
# /MONTH
# ==========================
app.add_handler(
    CommandHandler(
        "month",
        month
    )
)

# ==========================
# /HISTORY
# ==========================
app.add_handler(
    CommandHandler(
        "history",
        history
    )
)

# ==========================
# /SUMMARY
# ==========================
app.add_handler(
    CommandHandler(
        "summary",
        summary
    )
)

# ==========================
# /DELETE
# ==========================
app.add_handler(
    CommandHandler(
        "delete",
        delete
    )
)

# ==========================
# /UNDO
# ==========================
app.add_handler(
    CommandHandler(
        "undo",
        undo
    )
)

# ==========================
# /EDIT
# ==========================
app.add_handler(
    CommandHandler(
        "edit",
        edit_transaction
    )
)

# ==========================
# /HEALTH
# ==========================
app.add_handler(
    CommandHandler(
        "health",
        health
    )
)

# ==========================
# /ADMIN
# ==========================
app.add_handler(
    CommandHandler(
        "admin",
        admin
    )
)

# ==========================
# /EXPORT
# ==========================
app.add_handler(
    CommandHandler(
        "export",
        export
    )
)

# ==========================
# /SETBUDGET
# ==========================
app.add_handler(
    CommandHandler(
        "setbudget",
        setbudget
    )
)

print(
    "Bot Running..."
)
# print(app.handlers)

app.run_polling()

app.add_handler(
    MessageHandler(
        filters.COMMAND,
        unknown
    )
)