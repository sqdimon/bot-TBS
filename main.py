import telebot

bot = telebot.TeleBot('7341116778:AAGEPs3OYHCOwy-q4vTPHFS97-ZUZ91keI8')


@bot.message_handler(content_types=['text'])
def all_messages(message):
    bot.forward_message(367999688,message.chat.id, message.message_id)
    print (message)
if __name__ == '__main__':
    bot.polling(none_stop=True)
