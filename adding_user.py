from cfg import *


def adding_meneg(message):
    if message.text.lower() == 'бакалинская' or\
            message.text.lower() == 'бабушкина' or\
            message.text.lower() == 'жукова' or\
            message.text.lower() == 'достоевского' or\
            message.text.lower() == 'проспект' or\
            message.text.lower() == 'первомайская':
        return True


def add_user(message):
    office_val = (message.text.lower(),)
    sql_select_query = 'SELECT office_id from office WHERE office_address = ?'
    office_id = cur.execute(sql_select_query, (office_val)).fetchone()
    try:
        cur.execute('INSERT INTO user(chat_id, user_name, office_id) VALUES (?, ?, ?)',
                    (message.chat.id, message.chat.first_name, office_id[0]))
        bot.send_message(message.chat.id, 'Теперь ты есть в моей базе и можешь добавлять свои запчасти или '
                                          'искать запчасти других менеджеров. Введи команду /help что-бы увидеть список команд.')
        connection.commit()
    except sqlite3.IntegrityError as error:
        bot.send_message(message.chat.id, f'Так вышло, что ты уже есть в базе {error}')
