from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"
START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"

DEMO_CHANNEL = "https://t.me/demochannlink"
PREMIUM_CHANNEL = "https://t.me/howtogetpre"


# 🔹 START KEYBOARD
def start_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Get Premium", callback_data='premium')],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 Info", url=PREMIUM_CHANNEL)],
    ])


# 🔹 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=START_IMAGE,
        caption="🎬 Available Collection",
        reply_markup=start_keyboard()
    )


# 🔹 PREMIUM
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("👉 BASIC PLAN - ₹99", callback_data='plan1')],
        [InlineKeyboardButton("👉 STANDARD PLAN - ₹149", callback_data='plan2')],
        [InlineKeyboardButton("👉 ALL IN ONE - ₹249", callback_data='plan3')],
        [InlineKeyboardButton("👉 VIP ACCESS - ₹499", callback_data='plan4')],
        [InlineKeyboardButton("⬅ Back", callback_data='back')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.edit_media(
        media=telegram.InputMediaPhoto(
            media=PREMIUM_IMAGE,
            caption="💎 Select Your Plan:"
        ),
        reply_markup=reply_markup
    )


# 🔹 BACK
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.edit_media(
        media=telegram.InputMediaPhoto(
            media=START_IMAGE,
            caption="🎬 Available Collection"
        ),
        reply_markup=start_keyboard()
    )


# 🔹 BUTTON HANDLER
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "premium":
        await premium(update, context)

    elif data == "back":
        await back(update, context)


# 🔹 MAIN APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running...")
app.run_polling()
