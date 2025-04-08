from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread

# 🔐 Твой токен
BOT_TOKEN = '7788300571:AAEA3RHMKXdYmsVOU2VVs2syiqXne8ckQkY'
WEBAPP_URL = 'https://forms.gle/cUFMKRHXxZju7NDbA'

# ℹ️ Информация о компании
COMPANY_INFO = """🇷🇺 *О магазинах:*
*Bella Store* — это современный магазин косметики и парфюмерии в Бухаре.  
Мы предлагаем широкий ассортимент товаров и качественное обслуживание.  
Следите за нашими новинками и акциями через наши каналы:

---

🇺🇿 *Do‘konlar haqida:*
*Bella Store* — Buxorodagi zamonaviy kosmetika va parfyumeriya do‘koni.  
Keng assortiment va sifatli xizmat ko‘rsatish taklif qilamiz.  
Yangiliklar va aktsiyalarimizni kuzatib boring:

📲 [Instagram](https://instagram.com/bellastore_uz)  
📲 [Telegram](https://t.me/BellaStore_uz)
"""

# 👋 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    welcome_text = f"""
    Привет, {user_name}! 👋

    Мы рады, что вы заинтересовались вакансией в *Bella Store*! 🎉

    Если вы хотите стать частью нашей команды, нажмите на кнопку ниже, чтобы заполнить анкету. 👇
    """

    keyboard = [
        [
            KeyboardButton(text="📝 Заполнить анкету", web_app=WebAppInfo(url=WEBAPP_URL)),
            KeyboardButton(text="ℹ️ О нас")
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

    await update.message.reply_text(welcome_text, parse_mode='Markdown', reply_markup=reply_markup)

# ℹ️ Обработчик "О нас"
async def send_company_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "ℹ️ О нас":
        await update.message.reply_text(COMPANY_INFO, parse_mode='Markdown')

# ✅ Запуск телеграм-бота
def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), send_company_info))
    application.run_polling()

# 🌐 Flask сервер для поддержания активности
app = Flask('')

@app.route('/')
def home():
    return "✅ BellaStore бот работает! Phyton Разработчик 936515599"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run_web)
    thread.start()

# 🔁 Запуск всего
if __name__ == '__main__':
    keep_alive()
    run_bot()