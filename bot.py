from adding_user import *
from adding_info import *
from finder_parts import *
from cfg import *


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Привет {message.chat.first_name}!  Я бот, который поможет тебе избавиться от запчастей ')
    bot.send_message(message.chat.id,
                     'Давай выясним, в каком магазине ты работешь как тебя зовут. Напиши через запятую код магазина и имя (Например: UFK, Вадим):')


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
