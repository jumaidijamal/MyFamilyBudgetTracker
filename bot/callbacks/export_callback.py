from telegram.ext import CallbackQueryHandler

from bot.keyboards.export_keyboard import export_keyboard

from bot.handlers.export_handler import export


async def export_callback(update, context):

    query = update.callback_query

    await query.answer()

    data = query.data

    # ==========================
    # OPEN EXPORT MENU
    # ==========================

    if data == "admin_export":

        await query.edit_message_text(

            "📤 Export Menu\n\n"
            "Pilih format export.",

            reply_markup=export_keyboard()

        )

        return

    # ==========================
    # EXPORT CSV
    # ==========================

    if data == "export_csv":

        await query.delete_message()

        await export(update, context)

        return

    # ==========================
    # EXPORT EXCEL
    # ==========================

    if data == "export_excel":

        await query.answer(

            "🚧 Excel Export Coming Soon",

            show_alert=True

        )

        return

    # ==========================
    # EXPORT PDF
    # ==========================

    if data == "export_pdf":

        await query.answer(

            "🚧 PDF Export Coming Soon",

            show_alert=True

        )

        return


handler = CallbackQueryHandler(

    export_callback,

    pattern="^(admin_export|export_)"

)