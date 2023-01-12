from cfg import *


def show_car_brand_id(message):
    '''Составляет список брэндов автопроизводителей. Выгружает список из базы данных и отправляет, каждый
        id впаре с брендом, в отдельном сообщении'''
    sql_select_query = 'SELECT * from car_brand'
    brands = cur.execute(sql_select_query).fetchall()
    for i in brands:
        bot.send_message(message.chat.id, f'{i[0]} {i[1]}')


def find_car_id(infor):
    '''Находит id авто по введенному VIN'''
    sql_select_query = 'SELECT car_id from car WHERE car_vin= ?'
    info = (infor[4].upper(),)
    car_vin = cur.execute(sql_select_query, (info)).fetchone()
    return car_vin[0]


def instruction_add(message):
    '''Отправляет сообщение с инструкциями'''
    show_car_brand_id(message)
    bot.send_message(message.chat.id, 'Напиши через запятую:\n '
             'артикул детали (без пробелов и каких-либо знаков),\n'  # 0  part.part_art
             'название фимы,\n'  # 1 part.part_brand
             'краткую информацию о детали\n'  # 2 part.part_info
             'номер бренда авто\n'  # 3 car.car_brand_id
             'VIN автомобиля,\n'  # 4 car.car_vin 
             'Краткую информацию об авто -> ')  # 5 car.car_info
    return True


def inst(message):
    '''Функция затычка'''
    return True


def add_info(message):
    '''Добавляет деталь и машину в базу данных'''
    info = message.text.split(', ')
    print(f'add_info {info}')
    try:
        cur.execute('INSERT INTO car(car_brand_id, car_vin, car_info) VALUES (?, ?, ?)',
                                                                                (int(info[3]), info[4].upper(), info[5]))
        connection.commit()
        print('машита добавлена ')
        cur.execute('INSERT INTO part(part_art, part_brand, part_info, car_id, user_id) VALUES (?, ?, ?, ?, ?)',
                                                                (info[0].upper(), info[1], info[2], find_car_id(info), message.chat.id))
        connection.commit()
        print('деталь добавлена')
    except sqlite3.IntegrityError as error:
        print(f'эта машина уже добавлена -> {error}')
        cur.execute('INSERT INTO part(part_art, part_brand, part_info, car_id, user_id) VALUES (?, ?, ?, ?, ?)',
                                                                (info[0], info[1], info[2], find_car_id(info), message.chat.id))
        connection.commit()
        print('деталь добавлена')
    bot.send_message(message.chat.id, 'Информация успешно добавлена.')
