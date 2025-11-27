from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8412194208:AAF6lOZjqGq4-WVVxG9fWaaXUS2EB-pqVSE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("@corn_hub_channel - join the channel")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot started... 🚀")
app.run_polling()