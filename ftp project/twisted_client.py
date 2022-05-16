from twisted.internet import reactor , protocol
from twisted.internet.protocol import Protocol, ClientCreator

class TSClientProtocol(protocol.Protocol):
	def sendData(self):
		data = input("> ")
		if data:
			self.transport.write(data.encode())
		else:
			self.transport.loseConnection()

	def connectionMade(self):
		self.sendData()

	def dataReceived(self, data):
		recData = data.decode() # Конвертировать двоичные данные в строковые данные.
		print('Данные получены с сервера:% s' % (recData))
		self.sendData()
# 3, определить класс фабрики клиента
class TSClientFactory(protocol.ClientFactory):
	protocol = TSClientProtocol
	clientConnectionLost = clientConnectionFailed = lambda self, connector, reason:reactor.stop()
# 4, используйте реактор, чтобы начать соединение


HOST = 'localhost'
PORT = 2222
reactor.connectTCP(HOST, PORT, TSClientFactory())
reactor.run() # Стартовый цикл

'''
class Client(Protocol):
  def data_received(self, data):
    print(data)

  def send_message(self, message):
    self.transport.write( b'message')

def got_client(client):
  client.send_message('Hello!')
  reactor.callLater(5,client.send_message,'How are u?')

'''
"""                     
   ########################################
   ############## EXECUTION ###############
   ########################################


try:
  connection = ClientCreator(reactor,Client)
  connection.connectTCP(HOST,PORT).addCallback(got_client)

  reactor.run()
except:
  print('Client onnection error!')
"""