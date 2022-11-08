import telebot 
from Config_by_myToken_Algo import my_token
from telebot import types

bot = telebot.TeleBot(my_token)

@bot.message_handler(commands=['start'])
def start(msg):
    my_txt_hello = f'<u>Приветствую тебя, {msg.from_user.first_name} {msg.from_user.last_name}</u>'
    bot.send_message(msg.chat.id, my_txt_hello, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(msg):
    help_text = 'Я умею:\n/strat\n/help\n/game\n'
    bot.send_message(msg.chat.id, help_text)

@bot.message_handler(content_types=['photo'])
def photo_processing(msg):
    bot.send_message(msg.chat.id, 'Вау, какое классное фото!')

@bot.message_handler(commands=['game'])
def game(msg):
    txt_game = 'Спаси принцессу из замка\nПравила игры:\nВыбираем правильный путь до принцессы\nИстория.\nОднажды злая вошебница заточила принцессу в замке, потому что она была красивее неё.\nПройти надо дремучий лес, глубокое озеро, через ущелье'
    bot.send_message(msg.chat.id, txt_game)
    bot.send_message(msg.chat.id, 'Ты принц и стоишь на развилке у дремучего леса, у тебя есть 3 пути, какой ты выбирешь?')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Пойти в обход')
    btn2 = types.KeyboardButton('Пойти через саму чащу')
    btn3 = types.KeyboardButton('Повернуть назад, да ну эту принцессу)')
    markup.add(btn1, btn2, btn3)
    msg2 = bot.send_message(msg.chat.id, 'Куда пойдешь путник?', reply_markup=markup)
    bot.register_next_step_handler(msg2, continuation_game)

def continuation_game(msg):
    markup = types.ReplyKeyboardRemove(selective=False)
    if msg.text == 'Пойти в обход':
        msg2 = bot.send_message(msg.chat.id, 'Ты выбрал верный путь и идешь дальше',reply_markup=markup )
        bot.register_next_step_handler(msg2, step_field)
    elif msg.text == 'Пойти через саму чащу':
        msg2 = bot.send_message(msg.chat.id, 'Ты выбрал частично верный путь и тебе придется побороться, что бы не проиграть', reply_markup=markup)
        bot.register_next_step_handler(msg2, step_forest)
    else:
        bot.send_message(msg.chat.id, 'Ты проиграл.\nПопробуй еще раз')

def step_field(msg):
    markup = types.ReplyKeyboardMarkup(esize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')

def step_forest(msg):
    bot.send_message(msg.chat.id, 'Продолжение следует')


# @bot.message_handler(content_types=['text'])
# def word_processing(msg):
#     if msg.text == 'Hello':
#         bot.send_message(msg.chat.id, 'И тебе привет!)')
#     elif msg.text == 'id':
#         bot.send_message(msg.chat.id, msg.from_user.id)
#     elif msg.text == 'photo':
#         photo = open('05trmAch.jpg', 'rb')
#         bot.send_photo(msg.chat.id, photo)
#     elif msg.text != None:
#         bot.send_message(msg.chat.id, msg.text)
#     else:
#         bot.send_message(msg.chat.id, 'Я тебя не понимаю!')

bot.polling(none_stop = True)