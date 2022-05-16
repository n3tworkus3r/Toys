from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

class Connection(protocol.Protocol):

  def __init__(self):
    self.client_info = ""  # clientInfo сохранит информацию о клиентском соединении.

  def create_connection(self):
    self.client_info = self.transport.getPeer()

    self.factory.clients.append(self)
    print("Соединение с% s" % (self.client_info))

  def data_received(self, data):
    recieved_data = data.decode()
    print('Получены данные от % s: % s' % (self.client_info, recieved_data))
    rep = '[%s] %s' % (ctime(), recieved_data)
    self.transport.write(rep.encode())

  def lost_connection(self):
    self.factory.clients.remove(self)

  def line_received(self,line):
    for connection in self.factory.clients:
      if connection is not self:
        connection.sendLine(line)

class Server(protocol.Factory):
  def build_protocol(self, addr):
    return Connection()

  def startFactory(self):
    self.clients = []

'''                                        
   ########################################
   ############## EXECUTION ###############
   ########################################
'''
PORT = 2222
try:
  reactor.listenTCP(PORT, Server())
  print('Server listening on port {0}...'.format(PORT))
  reactor.run()
except:
  print('Connection error!')