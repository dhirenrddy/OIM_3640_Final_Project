from telegram.ext import Application, CommandHandler, ContextTypes # import core components for building a tg bot (aplication, handlers, and context types)
from telegram import Update # import the update class which represents an incoming message or command
from dotenv import load_dotenv # import the function to load env variables from .enc 
import os #import the os module to access BOT_TOKEN 
from events.loader import get_events_by_type # a function for /events_type

load_dotenv() # load BOT_TOKEN

import datetime # import datetime to handle time commands from user in bot
from events.loader import get_events_for_date, format_events # handles events based on date same as type

async def events_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    asynchronous function for the /events_today command
    asynchronous function can be paused and resumed, 
    allowing for non-blocking, asynchronous operations which is useful for a tg bot
    """
    print("✅ Received /events_today") # print confirmation to the terminal just for devs to see
    today = datetime.date.today().isoformat() # get the date in YYYY-MM-DD format
    events = get_events_for_date(today) # fetch events matching date from json
    await update.message.reply_text(format_events(events)) # ouput for the user

async def events_tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    asynchronous function for the /events_tomorrow command
    """
    print("✅ Received /events_tomorrow") # output in terminal
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat() # exactly the same format but for tomorrow
    events = get_events_for_date(tomorrow)
    await update.message.reply_text(format_events(events))

async def events_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ Received /events_date")
    if not context.args:
        await update.message.reply_text("Usage: /events_date YYYY-MM-DD")
        return
    date_str = context.args[0]
    events = get_events_for_date(date_str)
    await update.message.reply_text(format_events(events))

from events.loader import get_events_by_club

async def events_club(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ Received /events_club")
    if not context.args:
        await update.message.reply_text("Usage: /events_club ClubName")
        return
    club_name = " ".join(context.args)
    events = get_events_by_club(club_name)
    await update.message.reply_text(format_events(events))


async def events_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ Received /events_type")
    if not context.args:
        await update.message.reply_text("Usage: /events_type Workshop")
        return
    type_name = " ".join(context.args)
    events = get_events_by_type(type_name)
    await update.message.reply_text(format_events(events))


BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ Received /start")
    await update.message.reply_text("Hello! You can utilize the menu to see the events that interest you!")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("events_today", events_today))
app.add_handler(CommandHandler("events_tomorrow", events_tomorrow))
app.add_handler(CommandHandler("events_date", events_date))
app.add_handler(CommandHandler("events_club", events_club))
app.add_handler(CommandHandler("events_type", events_type))


print("🚀 Bot is running...")
app.run_polling()