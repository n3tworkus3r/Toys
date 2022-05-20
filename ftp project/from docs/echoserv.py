import time
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor, protocol
from twisted.protocols import basic


class Connection(basic.LineReceiver): # ЯВЛЯЕТСЯ ОБЪЕКТОМ PROTOCOL
  ####
  # Объект клиента на стороне сервера
  # Создаётся, когда клиент подключается
  def __init__(self):
    self.IP = ''
  ####

  def connectionMade(self):
    self.IP = self.transport.getPeer().host
    self.factory.clients.append(self)

    print("Online!",self.IP)



  def lineReceived(self, line):
    print(f"From {self.IP}:", repr(line))

    for c in self.factory.clients:
      c.message(line)

    msg = input('Enter a client message:')
    self.sendLine(msg.encode())

  def connectionLost(self, reason):
    self.factory.clients.remove(self)
    print("Disconnect",self.IP)

  def sendLine(self, line):
    return self.transport.write(line + self.delimiter)

  def message(self, message):
    self.transport.write(message)

class Server(protocol.ServerFactory):
  # Представляет собой сервер
  # Объединяет в себе lineReceiver-объекты (клиенты)

  protocol = Connection

  def startFactory(self):
    self.clients = []

  def changeClient(self):
    print('FUCK ME YEAH!')

  def stopFactory(self):
    print(self.clients)





port = 8000
reactor.listenTCP(port,Server())
print(f'Server listen port {port}')
reactor.run()
