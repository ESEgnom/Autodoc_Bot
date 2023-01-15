from cfg import *


def create_distribution_list():
    sql_select_query = 'SELECT chat_id from user'
    billet = cur.execute(sql_select_query).fetchall()
    print(type(billet))
    mail_list = []

    for item in billet:
        for jtem in item:
            mail_list.append(jtem)

    print(f'create_mail_list {mail_list}')
    return mail_list

def send_newsletter(message, part_info):
    distribution_list = create_distribution_list()
    sql_select_query = 'SELECT user_name FROM user where chat_id= ?'
    user_name = cur.execute(sql_select_query, (message.chat.id,)).fetchone()
    print(f'distribution_list {distribution_list}')
    print(f'billet {user_name} {type(user_name)}')

    for chat_id in distribution_list:
        if message.chat.id != chat_id:
            print(f'Сообщение для {chat_id}')
            print(f'{user_name[0]} добавил {part_info}')
            print(f'мой message.chat.id {message.chat.id}')
            bot.send_message(chat_id, f'{user_name[0]} добавил {part_info}')

