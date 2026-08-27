import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
CANAL = "@Dxsmultibot"
LIEN = "https://t.me/Dxsmultibot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    text = f"""🔱 DxS MULTI V14 🔱
━━━━━━━━━━━━━━━━━━━━
Salut {name} 👑

Bienvenue dans l'élite. Pour activer ton bot WhatsApp, tu dois valider ton accès.

📍 ÉTAPE OBLIGATOIRE :
👉 Rejoins @Dxsmultibot

C'est là-bas que tu auras les mises à jour, les nouveaux codes et le support.

Une fois fait, clique sur VÉRIFIER 👇
━━━━━━━━━━━━━━━━━━━━
⚡ 17 COMMANDS | AI | PAIRING
Dev by Kco4p tech"""

    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=LIEN)],
        [InlineKeyboardButton("✅ J'ai rejoint", callback_data="check")]
    ]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    try:
        m = await context.bot.get_chat_member(CANAL, query.from_user.id)
        ok = m.status not in ['left','kicked']
    except:
        ok = False
    if ok:
        await query.edit_message_text(f"🎉 Parfait {query.from_user.first_name} ! Accès validé ✅")
    else:
        await query.answer("❌ Tu n'as pas encore rejoint @Dxsmultibot", show_alert=True)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check))
    print("Bot DxS lancé...")
    app.run_polling()
