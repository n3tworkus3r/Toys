import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

###############################################################
######################## SERVER DATA ##########################
###############################################################

FTP_PORT = 2223
FTP_USER = "Y7V"
FTP_PASSWORD = "PSWD"
FTP_DIRECTORY = "/FTP"


def server_socket():
  HOST = socket.gethostname()
  PORT = 8000

  server_socket = socket.socket()
  server_socket.bind((HOST, PORT))
  server_socket.listen(10)

  client_socket, address = server_socket.accept()
  print('Connection from: {address} established'.format(address))

  while True:
    data = client_socket.recv(1024).decode()

    print("from connected user: " + str(data))
    data = input(' -> ')
    client_socket.send(data.encode())
  pass


def main():
  authorizer = DummyAuthorizer()
  authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

  handler = FTPHandler
  handler.authorizer = authorizer
  handler.banner = "pyftpdlib based ftpd ready."

  # Optionally specify range of ports to use for passive connections.
  #handler.passive_ports = range(60000, 65535)

  address = ('', FTP_PORT)
  server = FTPServer(address, handler)

  server.max_cons = 256
  server.max_cons_per_ip = 5

  server_socket()
  server.serve_forever()
  pass

"""
###############################################################
######################### EXECUTION ###########################
###############################################################
"""

if __name__ == '__main__':
 main()

