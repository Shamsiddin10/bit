import telebot
import os
import time
import logging

# 1. Loglarni sozlash (xatolarni kuzatish uchun)
logging.basicConfig(level=logging.INFO)

# 2. Tokenni Koyeb sozlamalaridan (Environment Variable) olamiz
# Agar kompyuterda sinab ko'rmoqchi bo'lsangiz, tokeningizni yozib qo'ying
TOKEN = os.getenv('BOT_TOKEN') or "SIZNING_TEST_TOKENINGIZ"
bot = telebot.TeleBot(TOKEN)

# --- BUYRUQLAR ---

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.reply_to(message, "Assalomu alaykum! 🤖\nMen Koyeb serverida 24/7 rejimida ishlaydigan botman.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Buyruqlar:\n/start - Ishga tushirish\n/help - Yordam")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

# --- 24/7 ISHLASH UCHUN POLLING ---

def run_bot():
    while True:
        try:
            print("Bot polling rejimida ishga tushdi...")
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            logging.error(f"Xatolik yuz berdi: {e}")
            time.sleep(10)  # 10 soniya kutib qayta urinadi

if __name__ == "__main__":
    run_bot()