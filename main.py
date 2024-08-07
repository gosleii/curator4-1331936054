import telebot

bot = telebot.TeleBot("7273907539:AAHxcGKbNLONyMNO1_qQEpWB4iqiefuz6a8")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(commands=["talk"])
def talk_handler(message):
    bot.send_message(message.chat.id, "*Как твои дела? *", parse_mode="Markdown")

@bot.message_handler(commands=["supermarket"])
def supermarket_handler(message):
    bot.send_message(message.chat.id, "*купить хлеб, молоко*", parse_mode="Markdown")

@bot.message_handler(commands=["homework"])
def homework_handler(message):
    bot.send_message(message.chat.id, "*Сделать и отправить боту*", parse_mode="Markdown")

bot.infinity_polling()