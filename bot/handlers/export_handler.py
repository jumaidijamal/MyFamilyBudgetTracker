from telegram import Update
from telegram.ext import ContextTypes

from config import (
    SPREADSHEET_ID
)

from services.sheet_service import (
    SheetService
)

from services.export_service import (
    ExportService
)


sheet_service = (
    SheetService(
        SPREADSHEET_ID
    )
)

export_service = (
    ExportService(
        sheet_service
    )
)


async def export(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # ==========================
    # HELP
    # ==========================

    if (
        not context.args
    ):

        await (
            update
            .message
            .reply_text(
                "📌 Format:\n\n"
                "/export month\n"
                "/export month csv\n"
                "/export month xlsx"
            )
        )

        return

    # ==========================
    # ARGUMENTS
    # ==========================

    mode = (
        context.args[0]
        .lower()
    )

    if mode != "month":

        await (
            update
            .message
            .reply_text(
                "Saat ini hanya "
                "/export month "
                "yang tersedia."
            )
        )

        return

    file_type = "csv"

    if (
        len(
            context.args
        )
        >= 2
    ):

        file_type = (
            context.args[1]
            .lower()
        )

    # ==========================
    # GENERATE FILE
    # ==========================

    try:

        if (
            file_type
            == "xlsx"
        ):

            filename = (
                export_service
                .export_month_xlsx()
            )

        else:

            filename = (
                export_service
                .export_month_csv()
            )

    except Exception as e:

        await (
            update
            .message
            .reply_text(
                f"❌ Export gagal.\n\n{str(e)}"
            )
        )

        return

    # ==========================
    # SEND FILE
    # ==========================

    try:

        with open(
            filename,
            "rb"
        ) as file:

            await (
                update
                .message
                .reply_document(
                    document=file,
                    filename=filename
                )
            )

    except Exception as e:

        await (
            update
            .message
            .reply_text(
                f"❌ Gagal mengirim file.\n\n{str(e)}"
            )
        )