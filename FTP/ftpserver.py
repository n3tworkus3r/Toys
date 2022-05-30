from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

###############################################################
######################## SERVER DATA ##########################
###############################################################

FTP_PORT = 60001
FTP_USER = "Y7V"
FTP_PASSWORD = "PSWD"
#FTP_DIRECTORY = "/FTP"
FTP_DIRECTORY = "D:\\FTP"


def main():
  authorizer = DummyAuthorizer()
  authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

  handler = FTPHandler
  handler.authorizer = authorizer
  handler.banner = "pyftpdlib based ftpd ready."

  # Optionally specify range of ports to use for passive connections.
  #handler.masquerade_address = '157.245.7.127'
  handler.passive_ports = range(60000, 65535)

  address = ('127.0.0.1', FTP_PORT)
  server = FTPServer(address, handler)

  server.max_cons = 256
  server.max_cons_per_ip = 5

  server.serve_forever()


"""
###############################################################
######################### EXECUTION ###########################
###############################################################
"""

if __name__ == '__main__':
 main()

