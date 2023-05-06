import telebot

bot = telebot.TeleBot("5906211167:AAFG-i9_ljPz_HR6Pwb_5uCfruU4ROmQt8M")

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key_markup.add("calculate BMI", "weight changes chart")

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "What can i do?", reply_markup = key_markup)

@bot.message_handler(func=lambda m: True)
def info(message):
    if message.text == "calculate BMI":
        msg = bot.send_message(message.chat.id, "Enter your weight in kg")
        bot.register_next_step_handler(msg, weight)

def weight(message):
    global wit
    wit = float(message.text)
    msg = bot.reply_to(message, "Enter your height in meter")
    bot.register_next_step_handler(msg, height)

def height(message):
    global hit
    hit = float(message.text)
    bmi = wit / (hit*hit)
    bot.send_message(message.chat.id, f"your BMI is: {round(bmi, 2)}")
    
bot.infinity_polling()