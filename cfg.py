import sqlite3
import telebot
from telebot import types

# bot = telebot.TeleBot('5807686063:AAFsIaAXr68ntBkl5oppMkM4B5Xs_oWzzGc')  #test
bot = telebot.TeleBot('5960126253:AAFOAdsevMU5euPB4xegsqSai0E4Nzg-8m4')

connection = sqlite3.connect('database.db', check_same_thread=False)
cur = connection.cursor()
print("База данных создана и успешно подключена к SQLite")