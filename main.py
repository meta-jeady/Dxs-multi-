import os, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
LIEN = "https://t.me/Dxsmultibot"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"DxS MULTI V14 Live")
def run_server():
    port = int(os.environ.get("PORT", 10000))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
threading.Thread(target=run_server, daemon=True).start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        query = update.callback_query
        user = query.from_user
        try:
            await query.message.delete()
        except:
            pass
        name = user.first_name
        text = f"""<b>🔱 𝗗𝘅𝗦 𝗠𝗨𝗟𝗧𝗜 𝗩𝟭𝟰 - 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗘𝗗𝗜𝗧𝗜𝗢𝗡 🔱</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝗛𝗲𝘆 {name} 👑
𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗘𝗹𝗶𝘁𝗲.

<b>⚙️ 𝗪𝗛𝗔𝗧 𝗬𝗢𝗨 𝗚𝗘𝗧 :</b>
├ 🤖 <b>𝟭𝟳 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>
├ 🛡️ <b>𝗔𝗻𝘁𝗶𝗹𝗶𝗻𝗸 & 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗔𝘂𝘁𝗼</b>
├ 🔗 <b>𝗜𝗻𝘀𝘁𝗮𝗻𝘁 𝗣𝗮𝗶𝗿𝗶𝗻𝗴 𝗖𝗼𝗱𝗲</b>
└ ⚡ <b>𝟮𝟰/𝟳 𝗙𝗮𝘀𝘁 & 𝗦𝘁𝗮𝗯𝗹𝗲</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"""
        kb = [
            [InlineKeyboardButton("📢 𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=LIEN)],
            [InlineKeyboardButton("🇫🇷 𝗙𝗿𝗮𝗻𝗰𝗮𝗶𝘀", callback_data="lang_fr"), InlineKeyboardButton("👨‍💻 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗗𝗘𝗩", url="https://t.me/metajeady")]
        ]
        with open("logo.jpg", "rb") as photo:
            await context.bot.send_photo(chat_id=user.id, photo=photo, caption=text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return

    name = update.effective_user.first_name
    text = f"""<b>🔱 𝗗𝘅𝗦 𝗠𝗨𝗟𝗧𝗜 𝗩𝟭𝟰 - 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗘𝗗𝗜𝗧𝗜𝗢𝗡 🔱</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝗛𝗲𝘆 {name} 👑
𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗘𝗹𝗶𝘁𝗲.

<b>⚙️ 𝗪𝗛𝗔𝗧 𝗬𝗢𝗨 𝗚𝗘𝗧 :</b>
├ 🤖 <b>𝟭𝟳 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀</b>
├ 🛡️ <b>𝗔𝗻𝘁𝗶𝗹𝗶𝗻𝗸 & 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗔𝘂𝘁𝗼</b>
├ 🔗 <b>𝗜𝗻𝘀𝘁𝗮𝗻𝘁 𝗣𝗮𝗶𝗿𝗶𝗻𝗴 𝗖𝗼𝗱𝗲</b>
└ ⚡ <b>𝟮𝟰/𝟳 𝗙𝗮𝘀𝘁 & 𝗦𝘁𝗮𝗯𝗹𝗲</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"""
    kb = [
        [InlineKeyboardButton("📢 𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=LIEN)],
        [InlineKeyboardButton("🇫🇷 𝗙𝗿𝗮𝗻𝗰𝗮𝗶𝘀", callback_data="lang_fr"), InlineKeyboardButton("👨‍💻 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗗𝗘𝗩", url="https://t.me/metajeady")]
    ]
    with open("logo.jpg", "rb") as photo:
        await update.message.reply_photo(photo=photo, caption=text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")

async def lang_fr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        await query.message.delete()
    except:
        pass
    name = query.from_user.first_name
    text = f"""<b>🔱 𝗗𝘅𝗦 𝗠𝗨𝗟𝗧𝗜 𝗩𝟭𝟰 - 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 🔱</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝗦𝗮𝗹𝘂𝘁 {name} 👑
𝗕𝗶𝗲𝗻𝘃𝗲𝗻𝘂𝗲 𝗱𝗮𝗻𝘀 𝗹'𝗘𝗹𝗶𝘁𝗲.

<b>⚙️ 𝗖𝗘 𝗤𝗨𝗘 𝗧𝗨 𝗔𝗨𝗥𝗔𝗦 :</b>
├ 🤖 <b>𝟭𝟳 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝗲𝘀 𝗣𝗿𝗲𝗺𝗶𝘂𝗺</b>
├ 🛡️ <b>𝗔𝗻𝘁𝗶𝗹𝗶𝗻𝗸 & 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗔𝘂𝘁𝗼</b>
├ 🔗 <b>𝗣𝗮𝗶𝗿𝗶𝗻𝗴 𝗜𝗻𝘀𝘁𝗮𝗻𝘁𝗮𝗻𝗲</b>
└ ⚡ <b>𝟮𝟰/𝟳 𝗦𝘁𝗮𝗯𝗹𝗲</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"""
    kb = [
        [InlineKeyboardButton("📢 𝗥𝗲𝗷𝗼𝗶𝗻𝗱𝗿𝗲 𝗖𝗮𝗻𝗮𝗹", url=LIEN)],
        [InlineKeyboardButton("🇬🇧 𝗘𝗻𝗴𝗹𝗶𝘀𝗵", callback_data="lang_en"), InlineKeyboardButton("👨‍💻 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗗𝗘𝗩", url="https://t.me/metajeady")]
    ]
    with open("logo.jpg", "rb") as photo:
        await context.bot.send_photo(chat_id=query.from_user.id, photo=photo, caption=text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(lang_fr, pattern="^lang_fr$"))
    app.add_handler(CallbackQueryHandler(start, pattern="^lang_en$"))
    print("DxS MULTI V14 Simple Live...")
    app.run_polling()
