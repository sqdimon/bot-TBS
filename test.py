import telebot

bot = telebot.TeleBot('7341116778:AAGEPs3OYHCOwy-q4vTPHFS97-ZUZ91keI8')

@bot.message_handler(func=lambda message: True)
def send_chat_id(message):
    bot.reply_to(message, f"Your Chat ID: {message.chat.id}")

bot.polling(none_stop=True)
