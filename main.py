import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# الرسالة الترحيبية الجديدة
welcome_message = "مرحباً بك! يا صانع المجد، كيف يمكنني مساعدتك؟"

# يرد على /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_message)

# يرد على أي رسالة بنفس الترحيب
@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.reply_to(message, welcome_message)

bot.infinity_polling()
