import socket
######################################
######### GLOBAL VARIABLES ###########
######################################

PORT = 8008
manager_address = ''
client_list = []
selected_client = ()

######################################
########## SERVER CREATING ###########
######################################

server_socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind (('localhost',PORT))

print (f'Server started at port {PORT}')

while True:
  data , address = server_socket.recvfrom(1024)
  message = data.decode()

  ########### NEW CONNECTION ###########
  if address not in client_list:
    print (f'{address[0]}, {address[1]} connected')
    client_list.append(address)
  ####### MANAGER IDENTIFICATION #######
  if 'Manager' in message:
    manager_address = address
  ########## SHOW CLIENT LIST ##########
  if 'show' in message:
    #print(f'CLIENTS: {client_list}')
    server_socket.sendto(f'CLIENTS: {client_list}'.encode(), manager_address)
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
  ######################################

