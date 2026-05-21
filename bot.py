from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ================= TOKEN =================
TOKEN = "YOUR_BOT_TOKEN"

# ================= IMAGES =================
START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"
PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"

# ================= LINKS =================
DEMO_CHANNEL = "https://t.me/demochannlink"
HOW_TO_CHANNEL = "https://t.me/howtogetpre"


# ================= START KEYBOARD =================
def start_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Get Premium", callback_data="premium")],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 How To Get Premium", url=HOW_TO_CHANNEL)],
    ])


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    caption = (
        "🎬 Available Videos Collection\n\n"
        "1. MOM Son Videos - 5000+\n"
        "2. Sister Brother Videos - 2000+\n"
        "3. Premium Videos - 15000+\n"
        "4. Teen Collection - 6000+\n"
        "5. Indian Desi Collection - 10000+\n"
        "6. Hidden Style Videos - 2000+"
    )

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        reply_markup=start_keyboard()
    )


# ================= PREMIUM MENU =================
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👉 BASIC PLAN - ₹99", callback_data="p1")],
        [InlineKeyboardButton("👉 STANDARD PLAN - ₹149", callback_data="p2")],
        [InlineKeyboardButton("👉 VIP PLAN 1 - ₹249", callback_data="p3")],
        [InlineKeyboardButton("👉 VIP PLAN 2 - ₹499", callback_data="p4")],
        [InlineKeyboardButton("⬅ Back", callback_data="back")]
    ])

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=PREMIUM_IMAGE,
            caption="💎 Select Your Plan Below 👇"
        ),
        reply_markup=keyboard
    )


# ================= BACK TO START =================
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=START_IMAGE,
            caption="🎬 Available Videos Collection"
        ),
        reply_markup=start_keyboard()
    )


# ================= CALLBACK HANDLER =================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "premium":
        await premium(update, context)

    elif data == "back":
        await back(update, context)

    elif data == "p1":
        await query.message.reply_text("✅ BASIC PLAN selected (₹99)")

    elif data == "p2":
        await query.message.reply_text("✅ STANDARD PLAN selected (₹149)")

    elif data == "p3":
        await query.message.reply_text("💎 VIP PLAN 1 selected (₹249)")

    elif data == "p4":
        await query.message.reply_text("🔥 VIP PLAN 2 selected (₹499)")


# ================= APP =================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running...")
app.run_polling()
