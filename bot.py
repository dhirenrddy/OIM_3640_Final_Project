from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import datetime
from config import BOT_TOKEN
from events.loader import (
    get_events_for_date,
    get_events_by_club,
    get_events_by_type,
    format_events,
)

async def events_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.date.today().isoformat()
    events = get_events_for_date(today)
    await update.message.reply_text(format_events(events))

async def events_tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    events = get_events_for_date(tomorrow)
    await update.message.reply_text(format_events(events))

async def events_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a date: /events_date YYYY-MM-DD")
        return
    date_str = context.args[0]
    events = get_events_for_date(date_str)
    await update.message.reply_text(format_events(events))

async def events_club(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a club name: /events_club ClubName")
        return
    club_name = " ".join(context.args)
    events = get_events_by_club(club_name)
    await update.message.reply_text(format_events(events))

async def events_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide an event type: /events_type TypeName")
        return
    type_name = " ".join(context.args)
    events = get_events_by_type(type_name)
    await update.message.reply_text(format_events(events))

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("events_today", events_today))
app.add_handler(CommandHandler("events_tomorrow", events_tomorrow))
app.add_handler(CommandHandler("events_date", events_date))
app.add_handler(CommandHandler("events_club", events_club))
app.add_handler(CommandHandler("events_type", events_type))

print(f"BOT_TOKEN is: {BOT_TOKEN}")

app.run_polling()