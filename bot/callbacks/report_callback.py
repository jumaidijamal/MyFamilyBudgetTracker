from bot.keyboards.report_keyboard import report_keyboard
from bot.keyboards.home_keyboard import home_keyboard

from bot.handlers.today_handler import today
from bot.handlers.week_handler import week
from bot.handlers.month_handler import month
from bot.handlers.history_handler import history
from bot.handlers.summary_handler import summary

from bot.handlers.today_handler import build_today_message


async def report_callback(update, context):

    query = update.callback_query

    await query.answer()
    
    print("REPORT CALLBACK")
    print(query.data)

    data = query.data

    if data == "menu_report":

        await query.edit_message_text(

            "📊 Report Center\n\n"
            "Silakan pilih jenis laporan.",

            reply_markup=report_keyboard()

        )

        return


    if data == "report_today":

        await query.edit_message_text(
            build_today_message()
        )
        return


    if data == "report_week":

        update.message = query.message
        await week(update, context)
        return


    if data == "report_month":

        update.message = query.message
        await month(update, context)
        return


    if data == "report_history":

        update.message = query.message
        await history(update, context)
        return


    if data == "report_summary":

        update.message = query.message
        await summary(update, context)
        return


    if data == "back_home":

        await query.edit_message_text(

            "💰 My Family Budget Tracker\n\n"
            "Silakan pilih menu.",

            reply_markup=home_keyboard()

        )