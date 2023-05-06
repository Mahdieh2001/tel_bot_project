import telebot

bot = telebot.TeleBot("5906211167:AAFG-i9_ljPz_HR6Pwb_5uCfruU4ROmQt8M")

first_button = telebot.types.InlineKeyboardButton("Button 1", url = "https://t.me/wasted_food_0")
second_button = telebot.types.InlineKeyboardButton("Button 2", callback_data="Hi!")

markup_hello = telebot.types.InlineKeyboardMarkup(row_width=1)

markup_hello.add(first_button, second_button)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    bot.answer_callback_query(call.id, "You clicked on hi!", show_alert=True)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi", reply_markup = markup_hello)

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key_markup.add("One", "Two", "Three")

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, "What can i do?", reply_markup = key_markup)

@bot.message_handler()
def keyboard(message):
    if message.text == "One":
        bot.send_message(message.chat.id, "You tapped on the first button.")
    elif message.text == "Two":
        bot.send_message(message.chat.id, "You tapped on the second button.")
    elif message.text == "Three":
        bot.send_message(message.chat.id, "You tapped on the third button.")

bot.infinity_polling()
