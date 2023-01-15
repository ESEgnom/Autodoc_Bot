from adding_user import *
from adding_info import *
from finder_parts import *
from cfg import *


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Привет {message.chat.first_name}!  Я бот, который поможет тебе избавиться от запчастей ')
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('/add_part')
    btn2 = types.KeyboardButton('/find_part')
    btn3 = types.KeyboardButton('/help')
    keyboard.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Давай выясним, в каком магазине ты работешь и как, ты хочешь что-бы тебя видели другие пользователи. '
                                           'Напиши через запятую код магазина и имя (Например: UFK, Вадим):',
                      reply_markup=keyboard)

@bot.message_handler(func=adding_meneg)
def add_user_handle(message):
    add_user(message)


@bot.message_handler(commands=['help'])
def show_commands(message):
    bot.send_message(message.chat.id, '/help\n/add_part\n/find_part')

@bot.message_handler(commands=['add_part'])
def show_add_part_instruction_handle(message):
    instruction_add(message)


@bot.message_handler(commands=['find_part'])
def show_find_part_instruction_handle(message):
    forward(message)


@bot.message_handler(func=broadcast)
def find_part_handle(message):
    find_parts(message)


@bot.message_handler(func=inst)
def add_part_handle(message):
    add_info(message)





if __name__ == '__main__':
    bot.infinity_polling()
