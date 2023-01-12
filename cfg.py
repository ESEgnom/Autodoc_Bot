import sqlite3
import telebot

bot = telebot.TeleBot('')


connection = sqlite3.connect('database.db', check_same_thread=False)
cur = connection.cursor()
print("База данных создана и успешно подключена к SQLite")