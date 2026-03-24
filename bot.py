import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = "@avrib"

SIGNATURE = "\n\n[אברהם בלוך מעדכן](https://linktr.ee/avribloch)"

KEYBOARD = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("לווטסאפ", url="https://whatsapp.com/channel/0029VaUqz5UCxoApmDGN4534"),
        InlineKeyboardButton("לטלגרם", url="https://t.me/avrib"),
    ]
])

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if not msg or not msg.text:
        return

    await context.bot.edit_message_text(
        chat_id=msg.chat_id,
        message_id=msg.message_id,
        text=msg.text + SIGNATURE,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=KEYBOARD,
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, handle_channel_post))
    print("🤖 הבוט פועל...")
    app.run_polling()

if __name__ == "__main__":
    main()
