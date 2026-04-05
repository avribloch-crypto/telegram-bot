import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8307141942:AAEQgAnEK17U1Tk-obyiikPqV_0oBGtmSMQ"
CHANNEL_ID = "@avrib"

SIGNATURE_TEXT = "הצטרפו לערוץ העדכונים של אברהם בלוך"
SIGNATURE_URL = "https://t.me/avrib"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("שלום! שלח לי טקסט ואני אפרסם בערוץ עם החתימה.")

async def post_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    keyboard = [[InlineKeyboardButton(SIGNATURE_TEXT, url=SIGNATURE_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=CHANNEL_ID, text=user_text, reply_markup=reply_markup)
    await update.message.reply_text("✅ הפוסט פורסם בערוץ עם החתימה!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, post_to_channel))
    app.run_polling()
