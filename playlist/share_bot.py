import sys
import time
import telepot
from telepot.loop import MessageLoop
import sqlite3


def send_to_all(playlist, user):
    bot = telepot.Bot('API_KEY')
    connection = sqlite3.connect('db.sqlite3')
    sql = "SELECT * from users_registered;"
    cursor = connection.cursor()
    cursor.execute(sql)
    for id, chat_id in cursor.fetchall():
        msg = "{}: veja minha playlist em {}".format(user, playlist)
        bot.sendMessage(chat_id, msg)
