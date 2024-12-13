import telebot

from smtp import send_message
from variables import BOT_TOKEN, EMAIL_PATTERN


destination = ''
waiting_for_message = False

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'email'])
def ask_email(message):
    bot.send_message(message.chat.id, 'Напишите свой email')


@bot.message_handler()
def handle_email(message):
    global destination
    global waiting_for_message

    successful = False

    if EMAIL_PATTERN.match(message.text):
        reply = 'Email написан правильно. Введите текст сообщения'
        destination = message.text
        waiting_for_message = True
    else:
        if waiting_for_message:
            reply, successful = send_message(destination, message.text)
        else:
            reply = 'Неправильный формат Email'

    bot.reply_to(message, reply)
    if successful:
        ask_email(message)
        destination = ''
        waiting_for_message = False


bot.infinity_polling()
