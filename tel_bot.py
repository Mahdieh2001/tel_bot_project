import telebot

bot = telebot.TeleBot("5906211167:AAFG-i9_ljPz_HR6Pwb_5uCfruU4ROmQt8M")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi")

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, "What can i do?")

bot.infinity_polling()