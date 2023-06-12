from transliterate import to_latin, to_cyrillic
import telebot
TOKEN = '6090940199:AAFbX0A7wFk8bkACLgDzp4OhqzxKKck8C04'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = 'Assalomu alaykum, krill-lotin botiga xush kelibsiz!'
    answer += '\nMatn kiriting:'
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg:to_cyrillic(msg)if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))

bot.polling()