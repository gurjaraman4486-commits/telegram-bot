from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"
PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"

DEMO_CHANNEL = "https://t.me/demochannlink"
PREMIUM_CHANNEL = "https://t.me/howtogetpre"


# MENU
def start_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Get Premium", callback_data="premium")],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 Info", url=PREMIUM_CHANNEL)],
    ])


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=START_IMAGE,
        caption="🎬 Available Collection",
        reply_markup=start_keyboard()
    )


# PREMIUM
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("👉 BASIC PLAN - ₹99", callback_data="p1")],
        [InlineKeyboardButton("⬅ Back", callback_data="back")]
    ]

    await query.message.delete()

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=PREMIUM_IMAGE,
        caption="💎 Select Your Plan:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# BACK
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.delete()

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=START_IMAGE,
        caption="🎬 Available Collection",
        reply_markup=start_keyboard()
    )


# HANDLER
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "premium":
        await premium(update, context)

    elif query.data == "back":
        await back(update, context)


# APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot running...")
app.run_polling()
