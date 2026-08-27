import os, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
CANAL = "@Dxsmultibot"
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
<b>📍 𝗠𝗔𝗡𝗗𝗔𝗧𝗢𝗥𝗬 :</b> 𝗝𝗼𝗶𝗻 @𝗗𝘅𝘀𝗺𝘂𝗹𝘁𝗶𝗯𝗼𝘁
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"""
        kb = [
            [InlineKeyboardButton("📢 𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=LIEN)],
            [InlineKeyboardButton("✅ 𝗩𝗲𝗿𝗶𝗳𝘆 𝗠𝘆 𝗔𝗰𝗰𝗲𝘀𝘀", callback_data="check")],
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
<b>📍 𝗠𝗔𝗡𝗗𝗔𝗧𝗢𝗥𝗬 :</b> 𝗝𝗼𝗶𝗻 @𝗗𝘅𝘀𝗺𝘂𝗹𝘁𝗶𝗯𝗼𝘁
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"""
    kb = [
        [InlineKeyboardButton("📢 𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=LIEN)],
        [InlineKeyboardButton("✅ 𝗩𝗲𝗿𝗶𝗳𝘆 𝗠𝘆 𝗔𝗰𝗰𝗲𝘀𝘀", callback_data="check")],
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
<b>📍 𝗢𝗕𝗟𝗜𝗚𝗔𝗧𝗢𝗜𝗥𝗘 :</b> 𝗥𝗲𝗷𝗼𝗶𝗻𝘀 @𝗗𝘅𝘀𝗺𝘂𝗹𝘁𝗶𝗯𝗼𝘁
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"""
    kb = [
        [InlineKeyboardButton("📢 𝗥𝗲𝗷𝗼𝗶𝗻𝗱𝗿𝗲 𝗖𝗮𝗻𝗮𝗹", url=LIEN)],
        [InlineKeyboardButton("✅ 𝗩𝗲𝗿𝗶𝗳𝗶𝗲𝗿", callback_data="check")],
        [InlineKeyboardButton("🇬🇧 𝗘𝗻𝗴𝗹𝗶𝘀𝗵", callback_data="lang_en"), InlineKeyboardButton("👨‍💻 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗗𝗘𝗩", url="https://t.me/metajeady")]
    ]
    with open("logo.jpg", "rb") as photo:
        await context.bot.send_photo(chat_id=query.from_user.id, photo=photo, caption=text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    try:
        m = await context.bot.get_chat_member(CANAL, query.from_user.id)
        ok = m.status not in ['left','kicked']
    except:
        ok = False
    if not ok:
        await query.answer("❌ Join @Dxsmultibot first!", show_alert=True)
        return
    await query.answer("✅ Access Granted")
    text = f"""<b>🔱 𝗗𝘅𝗦 𝗠𝗨𝗟𝗧𝗜 𝗩𝟭𝟰 | 𝗠𝗘𝗡𝗨 🔱</b>
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>
𝗛𝗲𝗹𝗹𝗼 {query.from_user.first_name} 👑
𝗔𝗰𝗰𝗲𝘀𝘀 𝗩𝗮𝗹𝗶𝗱𝗮𝘁𝗲𝗱 ✅
<b>📊 Status:</b> Premium Active
<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"""
    kb = [
        [InlineKeyboardButton("🤖 𝗣𝗮𝗶𝗿𝗶𝗻𝗴 𝗖𝗼𝗱𝗲", callback_data="pair"), InlineKeyboardButton("📜 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀", callback_data="cmds")],
        [InlineKeyboardButton("🛡️ 𝗔𝗻𝘁𝗶𝗹𝗶𝗻𝗸", callback_data="antilink"), InlineKeyboardButton("👋 𝗪𝗲𝗹𝗰𝗼𝗺𝗲", callback_data="welcome")],
        [InlineKeyboardButton("👥 𝗧𝗮𝗴𝗔𝗹𝗹", callback_data="tagall"), InlineKeyboardButton("👨‍💻 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗗𝗘𝗩", url="https://t.me/metajeady")]
    ]
    await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")

async def menu_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "pair":
        txt = "<b>🤖 𝗣𝗮𝗶𝗿𝗶𝗻𝗴 𝗠𝗼𝗱𝗲</b>\n\n𝗦𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 𝗻𝘂𝗺𝗯𝗲𝗿:\n<code>+22612345678</code>"
    elif data == "cmds":
        txt = """<b>📜 𝗗𝘅𝗦 𝗠𝗨𝗟𝗧𝗜 𝗩𝟭𝟰 - 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦</b>
<b>━━━━━━━━━━━━━━━━━━━━━━</b>
<b>🤖 𝗠𝗔𝗜𝗡 :</b>
├ <code>.menu</code> - Show bot menu
├ <code>.vv</code> - Open view once
├ <code>.tagall</code> - Tag all
├ <code>.hidetag</code> - Hidden tag
└ <code>.tag</code> - Tag with text

<b>🛡️ 𝗔𝗨𝗧𝗢 :</b>
├ <code>Antilink Auto</code>
├ <code>Welcome Auto</code>
└ <code>Antidelete</code>

<b>━━━━━━━━━━━━━━━━━━━━━━</b>"""
    elif data == "antilink":
        txt = "<b>🛡️ Antilink Auto</b>\n\nAuto delete links\n<code>.antilink on/off</code>"
    elif data == "welcome":
        txt = "<b>👋 Welcome Auto</b>\n\nAuto welcome\n<code>.welcome on/off</code>"
    elif data == "tagall":
        txt = "<b>👥 .tagall</b>\n\n<code>.tagall Hello</code>"
    elif data == "back":
        return await check(update, context)
    else:
        txt = f"<b>✅ {data.upper()} - Soon...</b>"
    
    kb = [[InlineKeyboardButton("🔙 𝗕𝗮𝗰𝗸", callback_data="back")]]
    await query.edit_message_caption(caption=txt, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check, pattern="^check$"))
    app.add_handler(CallbackQueryHandler(lang_fr, pattern="^lang_fr$"))
    app.add_handler(CallbackQueryHandler(start, pattern="^lang_en$"))
    app.add_handler(CallbackQueryHandler(menu_buttons))
    print("DxS MULTI V14 + LOGO Live...")
    app.run_polling()
