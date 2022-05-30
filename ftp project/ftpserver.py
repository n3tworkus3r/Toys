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
#FTP_DIRECTORY = "D:\\FTP"


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

  server.serve_forever()
  pass

"""
###############################################################
######################### EXECUTION ###########################
###############################################################
"""

if __name__ == '__main__':
 main()

