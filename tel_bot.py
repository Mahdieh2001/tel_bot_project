import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi")

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, "What can i do?")

bot.infinity_polling()