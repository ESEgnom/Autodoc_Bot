from cfg import *


def adding_meneg(message):
    msg = message.text.upper()
    if msg.startswith('UFU') or\
            msg.startswith('UFB') or\
            msg.startswith('UFK') or\
            msg.startswith('UFD') or\
            msg.startswith('UFP') or\
            msg.startswith('UFIM'):
        return True


def add_user(message):
    msg = message.text.upper()
    user_data_list = msg.split(', ')
    print(f'user_data_list {user_data_list} {type(user_data_list)}')
    user_data = user_data_list[0]
    print(f'user_data {user_data} {type(user_data)}')
    sql_select_query = 'SELECT office_id from office WHERE office_address = ?'
    office_id = cur.execute(sql_select_query, (user_data,)).fetchone()
    print(f'office_id {office_id}')
    try:
        cur.execute('INSERT INTO user(chat_id, user_name, office_id) VALUES (?, ?, ?)',
                    (message.chat.id, user_data_list[1], office_id[0]))
        bot.send_message(message.chat.id, 'Теперь ты есть в моей базе и можешь добавлять свои запчасти или '
                                          'искать запчасти других менеджеров. Введи команду /help что-бы увидеть список команд.')
        connection.commit()
    except sqlite3.IntegrityError as error:
        bot.send_message(message.chat.id, f'Так вышло, что ты уже есть в базе --> {error}')
