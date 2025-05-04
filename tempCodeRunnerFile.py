async def events_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print("✅ Received /events_type")
#     if not context.args:
#         await update.message.reply_text("Usage: /events_type Workshop")
#         return
#     type_name = " ".join(context.args)
#     events = get_events_by_type(type_name)
#     await update.message.reply_text(format_events(events))