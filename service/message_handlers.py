import get_memes.ninegag
from service.bot import animal_bot


@animal_bot.message_handler(commands=['start'])
def start(message):
    animal_bot.send_message(message.chat.id, 'hi!', parse_mode='html')
    get_memes.ninegag.get_meme()

@animal_bot.message_handler(commands=['hi'])
def hi(message):
    animal_bot.send_message(message.chat.id, 'hi!', parse_mode='html')


animal_bot.polling(none_stop=True)