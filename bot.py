from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "8919459210:AAGWtjHwgUFETIABPIVTOrhB2dcgGFvMLBc"

PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"

DEMO_CHANNEL = "https://t.me/demochannlink"
PREMIUM_CHANNEL = "https://t.me/howtogetpre"

START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"


def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data='premium')],
        [InlineKeyboardButton("📢 Demo", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 Info", url=PREMIUM_CHANNEL)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = "🔥 *Available Collection*\nChoose an option below 👇"

    update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


def premium(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("👉 BASIC PLAN - ₹99", callback_data='plan1')],
        [InlineKeyboardButton("👉 STANDARD PLAN - ₹149", callback_data='plan2')],
        [InlineKeyboardButton("👉 ALL IN ONE - ₹249", callback_data='plan3')],
        [InlineKeyboardButton("👉 VIP ACCESS - ₹499", callback_data='plan4')],
        [InlineKeyboardButton("⬅ Back", callback_data='back')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.edit_caption(
        caption="💎 Select Your Plan:",
        reply_markup=reply_markup
    )

def back(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("💎 Get Premium", callback_data='premium')],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 Info", url=PREMIUM_CHANNEL)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.edit_text(
        "🎬 Available Collection\n\nChoose an option below 👇",
        reply_markup=reply_markup
    )

def handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    print("BUTTON CLICKED:", query.data)

    if query.data == 'premium':
        premium(update, context)
      
    if query.data == 'back':
        back(update, context)


updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(handler))

updater.start_polling()
updater.idle()
