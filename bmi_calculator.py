import telebot

bot = telebot.TeleBot("5906211167:AAFG-i9_ljPz_HR6Pwb_5uCfruU4ROmQt8M")

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_markup.add("calculate BMI")

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
    msg = bot.reply_to(message, "Enter your height in centimeter")
    bot.register_next_step_handler(msg, height)

def height(message):
    global hit
    hit = float(message.text)
    bmi = wit*10000 / (hit*hit)
    if (bmi < 18.5):
        health_condition = "underweight"
  
    elif ( bmi >= 18.5 and bmi < 24.9):
        health_condition = "healthy"
  
    elif ( bmi >= 24.9 and bmi < 30):
        health_condition = "overweight"
  
    elif ( bmi >=30):
        health_condition = "suffering from Obesity"

    bot.send_message(message.chat.id, f"your BMI is: {round(bmi, 2)}\n \nYou are {health_condition}")
    
bot.infinity_polling()