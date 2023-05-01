import telebot

bot = telebot.TeleBot("")

first_button = telebot.types.InlineKeyboardButton("Button 1", url = "https://t.me/wasted_food_0")
second_button = telebot.types.InlineKeyboardButton("Button 2", url = "https://www.theodinproject.com/dashboard")

markup_hello = telebot.types.InlineKeyboardMarkup()
markup_help = telebot.types.InlineKeyboardMarkup(row_width=1)

markup_hello.add(first_button, second_button)
markup_help.add(first_button, second_button)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi", reply_markup = markup_hello)

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, "What can i do?", reply_markup = markup_help)

bot.infinity_polling()
