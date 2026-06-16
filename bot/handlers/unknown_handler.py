import difflib

from telegram import Update
from telegram.ext import ContextTypes


COMMANDS = [

    "/start",
    "/help",
    "/update",
    "/edit",
    "/delete",
    "/balance",
    "/today",
    "/week",
    "/month",
    "/history",
    "/summary",
    "/health",
    "/admin",
    "/export",
    "/budget",
    "/setbudget",
    "/reminder"
]


async def unknown(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        update
        .message
        .text
        .split()[0]
        .lower()
    )

    suggestions = (
        difflib.get_close_matches(
            text,
            COMMANDS,
            n=1,
            cutoff=0.4
        )
    )

    message = (
        "❌ Command tidak dikenal."
    )

    if suggestions:

        message += (
            "\n\nMungkin maksud Anda:\n"
            f"{suggestions[0]}"
        )

    message += (
        "\n\nGunakan /help "
        "untuk melihat daftar command."
    )

    await (
        update
        .message
        .reply_text(
            message
        )
    )