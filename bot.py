from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

import sqlite3
import time

# ================= CONFIG =================

TOKEN = "8919459210:AAGWtjHwgUFETIABPIVTOrhB2dcgGFvMLBc"

ADMIN_ID = 6648941928

UPI_ID = "paytm.s1myjcl@pty"

FORCE_CHANNEL = "@pvtmmsvdo"

START_IMAGE = "https://i.postimg.cc/MKWZn3Lv/IMG-20260521-163611-172.jpg"

PREMIUM_IMAGE = "https://i.postimg.cc/x89kTfHG/IMG-20260521-164434-789.jpg"

# ================= DATABASE =================

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    premium INTEGER DEFAULT 0,
    expiry INTEGER DEFAULT 0
)
""")

conn.commit()

# ================= FUNCTIONS =================

def add_user(user_id, username):
    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id, username) VALUES(?, ?)",
        (user_id, username)
    )
    conn.commit()


def make_premium(user_id, days=30):

    expiry = int(time.time()) + (days * 86400)

    cursor.execute(
        "UPDATE users SET premium=1, expiry=? WHERE user_id=?",
        (expiry, user_id)
    )

    conn.commit()


def remove_expired():

    now = int(time.time())

    cursor.execute(
        "UPDATE users SET premium=0 WHERE expiry < ?",
        (now,)
    )

    conn.commit()


def total_users():

    cursor.execute("SELECT COUNT(*) FROM users")

    return cursor.fetchone()[0]


# ================= FORCE JOIN =================

async def check_join(user_id, bot):

    try:
        member = await bot.get_chat_member(FORCE_CHANNEL, user_id)

        return member.status in ["member", "administrator", "creator"]

    except:
        return False


# ================= KEYBOARD =================

def start_keyboard():

    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Get Premium", callback_data="premium")],
        [InlineKeyboardButton("🎬 Demo Videos", url="https://t.me/demochannlink")],
        [InlineKeyboardButton("📖 How To Get Premium", url="https://t.me/howtogetpre")]
    ])


# ================= START =================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(user.id, user.username)

    remove_expired()

    joined = await check_join(user.id, context.bot)

    if not joined:

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Join Channel", url=f"https://t.me/{FORCE_CHANNEL.replace('@','')}")],
            [InlineKeyboardButton("✅ Joined", callback_data="joined")]
        ])

        await update.message.reply_text(
            "⚠️ First Join Our Channel",
            reply_markup=keyboard
        )

        return

    caption = (
        "<b>🎬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧</b>\n\n"

        "<b>➊ 𝐌𝐎𝐌 𝐒𝐨𝐧 𝐕𝐢𝐝𝐞𝐨𝐬 - 𝟓𝟎𝟎𝟎+</b>\n\n"

        "<b>➋ 𝐒𝐢𝐬𝐭𝐞𝐫 𝐁𝐫𝐨𝐭𝐡𝐞𝐫 𝐕𝐢𝐝𝐞𝐨𝐬 - 𝟐𝟎𝟎𝟎+</b>\n\n"

        "<b>➌ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐕𝐢𝐝𝐞𝐨𝐬 - 𝟏𝟓𝟎𝟎𝟎+</b>\n\n"

        "<b>➍ 𝐓𝐞𝐞𝐧 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧 - 𝟔𝟎𝟎𝟎+</b>\n\n"

        "<b>➎ 𝐈𝐧𝐝𝐢𝐚𝐧 𝐃𝐞𝐬𝐢 𝐂𝐨𝐥𝐥𝐞𝐜𝐭𝐢𝐨𝐧 - 𝟏𝟎𝟎𝟎𝟎+</b>\n\n"

        "<b>➏ 𝐇𝐢𝐝𝐝𝐞𝐧 𝐒𝐭𝐲𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 - 𝟐𝟎𝟎𝟎+</b>"
    )

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        parse_mode="HTML",
        reply_markup=start_keyboard()
    )


# ================= PREMIUM =================

async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👉 BASIC PLAN - ₹99", callback_data="buy_99")],
        [InlineKeyboardButton("👉 STANDARD PLAN - ₹149", callback_data="buy_149")],
        [InlineKeyboardButton("👉 VIP PLAN 1 - ₹249", callback_data="buy_249")],
        [InlineKeyboardButton("👉 VIP PLAN 2 - ₹499", callback_data="buy_499")],
        [InlineKeyboardButton("⬅ Back", callback_data="back")]
    ])

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=PREMIUM_IMAGE,
            caption="<b>💎 𝐒𝐞𝐥𝐞𝐜𝐭 𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧 👇</b>",
            parse_mode="HTML"
        ),
        reply_markup=keyboard
    )


# ================= BUY =================

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    amount = query.data.split("_")[1]

    text = (
        f"<b>💸 Send Payment Here</b>\n\n"
        f"<code>{UPI_ID}</code>\n\n"
        f"<b>Amount: ₹{amount}</b>\n\n"
        f"📸 Send Screenshot After Payment"
    )

    await query.message.reply_text(
        text,
        parse_mode="HTML"
    )


# ================= SCREENSHOT =================

async def screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✅ Approve",
                callback_data=f"approve_{user.id}"
            )
        ]
    ])

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=update.message.photo[-1].file_id,
        caption=f"💰 Payment From @{user.username}",
        reply_markup=buttons
    )

    await update.message.reply_text(
        "✅ Screenshot Submitted"
    )


# ================= APPROVE =================

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    user_id = int(query.data.split("_")[1])

    make_premium(user_id)

    await context.bot.send_message(
        chat_id=user_id,
        text="🎉 Premium Activated For 30 Days"
    )

    await query.edit_message_caption(
        caption="✅ Approved"
    )


# ================= BROADCAST =================

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    if len(context.args) == 0:
        return await update.message.reply_text(
            "Use:\n/broadcast message"
        )

    msg = " ".join(context.args)

    cursor.execute("SELECT user_id FROM users")

    users = cursor.fetchall()

    success = 0

    for user in users:

        try:
            await context.bot.send_message(user[0], msg)

            success += 1

        except:
            pass

    await update.message.reply_text(
        f"✅ Broadcast Sent To {success} Users"
    )


# ================= STATS =================

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    users = total_users()

    await update.message.reply_text(
        f"👥 Total Users: {users}"
    )


# ================= BACK =================

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    await start(update, context)


# ================= HANDLER =================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    data = query.data

    if data == "premium":

        await premium(update, context)

    elif data == "back":

        await back(update, context)

    elif data.startswith("buy_"):

        await buy(update, context)

    elif data.startswith("approve_"):

        await approve(update, context)

    elif data == "joined":

        await start(update, context)


# ================= APP =================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("broadcast", broadcast))

app.add_handler(CommandHandler("stats", stats))

app.add_handler(CallbackQueryHandler(button_handler))

app.add_handler(MessageHandler(filters.PHOTO, screenshot))

print("Bot Running...")

app.run_polling()
