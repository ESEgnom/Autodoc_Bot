from cfg import *

def forward(message):
    bot.send_message(message.chat.id, 'Напиши мне артикул детали (без пробелов и каких-либо знаков), '
                                      'я попробую что нибудь найти в базе: ')


def broadcast(message):
    print(f'finder_parts.broadcast ({message.text})')
    art = message.text.split(', ')
    if len(art) != 5:
        return True
    else:
        return False



def find_parts(message):
    sql_select_query = 'SELECT part.part_brand, ' \
                       'part.part_art, ' \
                       'part.part_info, ' \
                       'car.car_vin AS vin, ' \
                       'car.car_info AS car_info, ' \
                       'user.user_name AS user_name, ' \
                       'office.office_address AS office from part ' \
                       'JOIN car ON part.car_id = car.car_id JOIN user ON part.user_id = user.chat_id JOIN office on user.office_id = office.office_id WHERE part.part_art=?'
    art = (message.text.upper(),)
    info = cur.execute(sql_select_query, (art)).fetchall()
    print(f'finder_parts.find_parts {info}')
    if len(info) > 0:
        bot.send_message(message.chat.id, f'Есть! Нашел! Это:\n {info[0][0]}\n'
                                          f'{info[0][2]}\nартикул: {info[0][1]}\n'
                                          f'{info[0][4]}\n {info[0][3]}')

        for item in info:
            bot.send_message(message.chat.id, f'{item[5]} магазин {item[6]}')
    else:
        bot.send_message(message.chat.id, 'К сожалению эту запчасть еще ни кто не добавил')



