from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ================= TOKEN =================
TOKEN = "8919459210:AAGWtjHwgUFETIABPIVTOrhB2dcgGFvMLBc"

# ================= IMAGES =================
START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"
PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"

# ================= LINKS =================
DEMO_CHANNEL = "https://t.me/demochannlink"
INFO_CHANNEL = "https://t.me/howtogetpre"


# ================= START KEYBOARD =================
def start_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Get Premium", callback_data="premium")],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 How To Get Premium", url=INFO_CHANNEL)],
    ])


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    caption = (
        "<b>🎬 Available Videos Collection</b>\n\n"
        "<b>1. MOM Son Videos - 5000+</b>\n"
        "<b>2. Sister Brother Videos - 2000+</b>\n"
        "<b>3. Premium Videos - 15000+</b>\n"
        "<b>4. Teen Collection - 6000+</b>\n"
        "<b>5. Indian Desi Collection - 10000+</b>\n"
        "<b>6. Hidden Style Videos - 2000+</b>"
    )

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        parse_mode="HTML",
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
            caption="<b>💎 Select Your Plan Below 👇</b>",
            parse_mode="HTML"
        ),
        reply_markup=keyboard
    )


# ================= BACK =================
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    caption = "<b>🎬 Available Videos Collection</b>"

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=START_IMAGE,
            caption=caption,
            parse_mode="HTML"
        ),
        reply_markup=start_keyboard()
    )


# ================= HANDLER =================
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


# ================= RUN =================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running...")
app.run_polling()
