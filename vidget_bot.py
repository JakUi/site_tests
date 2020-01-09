# -*- coding: utf-8 -*-
import telebot
from telebot import apihelper
import requests
from threading import Thread
from config import TOKEN
import time
import datetime

bot = telebot.TeleBot(TOKEN)
set_of_members = set() #промежуточное множество 
event = False
###!!!!!!!!!!!!!!!!!!!
#####Для работы с нашим прокси нужно в файле apihelper.py библиотеки telebot заменить
#API_URL = "https://api.telegram.org/bot{0}/{1}"
#FILE_URL = "https://api.telegram.org/file/bot{0}/{1}"
#на:
#API_URL = "https://api-tg.ksdev.ru/bot{0}/{1}"
#FILE_URL = "https://api-tg.ksdev.ru/file/bot{0}/{1}"

@bot.message_handler(content_types=["text"])
def process_start_command(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, "Привет!\n Я добавил тебя в свой список оповещений.")
        x_id = message.from_user.id
        x_id = str(x_id)
        set_of_members.add(x_id)#добавляем в множество user_id
        f_users = open('users.txt', 'a') #открываем файл на запись (дозаписываем в конец, не удаляя)
        for member in set_of_members: 
            f_users.write(member + ', ') #записываем всех пользователей из множества в файл
        f_users.close() #закрываем файл

widget_sended = False #флажок, означает, что месседж о том, что Охта закрыта был отправлен
widget_cancel_event = False #флажок, означает, что месседж о том, что Охта открыта был отправлен
widget_event = False #тригер. False - виджет работает
site_sended = False
site_cancel_event = False
site_event = False
###При рассылке сообщений все id из файла f_users сначала переносим в множество set_of_recepient (чтобы не дублировать id получателей), а затем рассылку делаем из списка set_of_recepient 
# отправка сообщений без handlera!

bot = telebot.TeleBot(TOKEN)
set_of_recipient = set() #объявляем множество получателей
all_users = open('users.txt', 'r') #открываем файл со списком пользователей бота на чтение
lines = all_users.read().split(', ') #читаем файл по словам
for i in range (0, len(lines)):
    set_of_recipient.add(lines[i]) #в множество записываем id каждого пользователя
all_users.close()
set_of_recipient = list(set_of_recipient) #преобразуем множество в список

def send_widget_bad(set_of_recipient):
    send = 'Виджет упал!'
    for i in range(0, len(set_of_recipient)):
        if set_of_recipient[i] != '':
            chatId = set_of_recipient[i]#chatId берем из списка получателей первый символ пропускаем т.к. это пробел
            print('chatid=', chatId)
            bot.send_message(chatId, send)
    
def send_widget_cancel(set_of_recipient):
    send = 'Виджет снова в строю!' 
    for i in range(0, len(set_of_recipient)):
        if set_of_recipient[i] != '':
            chatId = set_of_recipient[i] #chat Id берем из списка получателей
            print('chatid=', chatId)
            bot.send_message(chatId, send)

def send_site_bad(set_of_recipient):
    send = 'Сайт не доступен!'
    for i in range(0, len(set_of_recipient)):
        if set_of_recipient[i] != '':
            chatId = set_of_recipient[i]#chatId берем из списка получателей первый символ пропускаем т.к. это пробел
            print('chatid=', chatId)
            bot.send_message(chatId, send)
    
def send_site_cancel(set_of_recipient):
    send = 'Сайт снова в строю!' 
    for i in range(0, len(set_of_recipient)):
        if set_of_recipient[i] != '':
            chatId = set_of_recipient[i] #chat Id берем из списка получателей
            print('chatid=', chatId)
            bot.send_message(chatId, send)

    
def monitoring(widget_sended, widget_cancel_event, widget_event, site_sended, site_cancel_event, site_event):
    while True:
        time.sleep(60.0) #пауза между запросами
        r = requests.get('https://widget.planoplan.com/998ac5edf6bc4759696f31fa070e922a') #запрос. Виджет находится на странице developers
        started = requests.get('https://planoplan.com')
        #r = requests.get('https://widget.planoplan.com/9114405bf9eb0ecf6014a8ce9f6f44c2') #запрос. Тестовый виджет
        if r.status_code != requests.codes.ok:
            widget_event = True
        elif r.status_code == requests.codes.ok:
            if widget_event == True: 
                widget_event = False
                send_widget_cancel(set_of_recipient)
                widget_sended = False
                print('end')
        elif started.status_code != requests.codes.ok:
            site_event = True
        elif started.status_code == requests.codes.ok:
            if site_event == True: 
                site_event = False
                send_site_cancel(set_of_recipient)
                site_sended = False
                print('end')
        if widget_event == True and widget_sended == False: #если виджет не доступен отправляем сообщение 
            send_widget_bad(set_of_recipient)
            widget_sended = True #флажок, означает, что месседж о том, что виджет лежит был отправлен
        elif site_event == True and site_sended == False: #если сайт не доступен отправляем сообщение 
            send_site_bad(set_of_recipient)
            site_sended = True #флажок, означает, что месседж о том, что сайт лежит был отправлен

def ex():            
    bot.polling(none_stop=True, timeout=600, interval=0)
        
thread1 = Thread(target = monitoring, args = (widget_sended, widget_cancel_event, widget_event, site_sended, site_cancel_event, site_event))
thread2 = Thread(target = ex)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
