from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8919459210:AAGWtjHwgUFETIABPIVTOrhB2dcgGFvMLBc"

START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"
PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"

DEMO_CHANNEL = "https://t.me/demochannlink"
INFO_CHANNEL = "https://t.me/howtogetpre"


# ================= START KEYBOARD =================
def start_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Get Premium", callback_data="premium")],
        [InlineKeyboardButton("🎬 Demo Videos", url=DEMO_CHANNEL)],
        [InlineKeyboardButton("📖 Info", url=INFO_CHANNEL)],
    ])


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    caption = """🎬 Available Collection

🎬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧

𝟏. 𝐌𝟎𝐌 𝐒𝐨𝐧 𝐯𝐢𝐝𝐞𝐨𝐬 - 𝟓𝟎𝟎𝟎+

𝟐. 𝐒𝐢𝐬𝐭𝐞𝐫 𝐁𝐫𝐨𝐭𝐡𝐞𝐫 𝐯𝐢𝐝𝐞𝐨𝐬 - 𝟐𝟎𝟎𝟎+

𝟑. 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐕𝐢𝐝𝐞𝐨𝐬 - 𝟏𝟓𝟎𝟎𝟎+

𝟒. 𝟏𝟖+ 𝐓𝐞𝐞𝐧 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧 - 𝟔𝟎𝟎𝟎+

𝟓. 𝐈𝐧𝐝𝐢𝐚𝐧 𝐃𝐞𝐬𝐢 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧 - 𝟏𝟎𝟎𝟎𝟎+

𝟔. 𝐇𝐢𝐝𝐝𝐞𝐧 𝐂𝐚𝐦 𝐒𝐭𝐲𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 - 𝟐𝟎𝟎𝟎+"""

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        reply_markup=start_keyboard()
    )


# ================= PREMIUM =================
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


# ================= BACK =================
async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=START_IMAGE,
            caption="🎬 Available Collection"
        ),
        reply_markup=start_keyboard()
    )


# ================= HANDLER =================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "premium":
        await premium(update, context)

    elif query.data == "back":
        await back(update, context)

    elif query.data == "p1":
        await query.message.reply_text("✅ BASIC PLAN selected")

    elif query.data == "p2":
        await query.message.reply_text("✅ STANDARD PLAN selected")

    elif query.data == "p3":
        await query.message.reply_text("✅ VIP PLAN 1 selected")

    elif query.data == "p4":
        await query.message.reply_text("💎 VIP PLAN 2 selected (₹499)")


# ================= RUN =================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot running...")
app.run_polling()
