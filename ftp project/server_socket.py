
import time
import select
import socket


def main_menu(server_socket):
  while True:
    print('\n\t\tMENU:\n'
    '[sh-c] - show client\n'
    '[sl] - select user\n')

    key = input('Enter a command: ')
    match key:
      case 'sh-c':
        show_client(server_socket)
      case 'sl':
        select_user()
  pass

def show_connection_list(inputs):
  connection_list = ''
  for i in range(len(inputs)-1):
    connection_list += '\n' + str(inputs[i+1])
  return connection_list





def server_program():
  #host = socket.gethostname()
  #host = '143.244.145.116'
  port = 8000  # initiate port no above 1024



  print('Для выключения сервера нажмите Ctrl+C.')
  server_socket = socket.socket()
  host = socket.gethostname()
  server_socket.bind((host, port))
  server_socket.listen(5)
  server_socket.setblocking(False)

  inputs = [server_socket]  # сокеты, которые будем читать
  outputs = []  # сокеты, в которые надо писать
  messages = {}  # здесь будем хранить сообщения для сокетов

  print('\nОжидание подключения...')
  while True:
    # вызов `select.select` который проверяет сокеты в
    # списках: `inputs`, `outputs` и по готовности, хотя бы
    # одного - возвращает списки: `reads`, `send`, `excepts`
    reads, send, excepts = select.select(inputs, outputs, inputs)

    # Далее проверяются эти списки, и принимаются
    # решения в зависимости от назначения списка

    # список READS - сокеты, готовые к чтению
    for connection in reads:
      if connection == server_socket:
        # если это серверный сокет, то пришел новый
        # клиент, принимаем подключение
        client_connection, client_address = connection.accept()
        print('Connection established: {0}'.format(client_address))
        # устанавливаем неблокирующий сокет
        client_connection.setblocking(False)
        # поместим новый сокет в очередь
        # на прослушивание
        inputs.append(client_connection)

      else:
        # если это НЕ серверный сокет, то
        # клиент хочет что-то сказать
        data = connection.recv(1024)
        if data:
          # если сокет прочитался и есть сообщение
          # то кладем сообщение в словарь, где
          # ключом будет сокет клиента
          if messages.get(connection, None):
            messages[connection].append(data)
          else:
            messages[connection] = [data]

          # добавляем соединение клиента в очередь
          # на готовность к приему сообщений от сервера
          if connection not in outputs:
            outputs.append(connection)
        else:
          print('Клиент отключился...')
          # если сообщений нет, то клиент
          # закрыл соединение или отвалился
          # удаляем его сокет из всех очередей
          if connection in outputs:
            outputs.remove(connection)
          inputs.remove(connection)
          # закрываем сокет как положено, тем
          # самым очищаем используемые ресурсы
          connection.close()
          # удаляем сообщения для данного сокета
          del messages[connection]
#########################################################################
#########################################################################
#########################################################################
    # список SEND - сокеты, готовые принять сообщение
    for connection in send:
      # выбираем из словаря сообщения
      # для данного сокета
      msg_list = messages.get(connection, None)
      if len(msg_list):
        temp = ''
        # если есть сообщения - то переводим
        # его "в верхний регистр и отсылаем
        #for message in msg_list:

        match msg_list[len(msg_list)-1]:
          case b'connection list': # Сообщение от manager == connection list
            temp = show_connection_list(inputs)
            connection.send(temp.encode())
          #case b'select connection':
          #  connection = input('hueta!')

        if  b'select connection' in msg_list[len(msg_list)-1]:
          message = str(msg_list[len(msg_list)-1])
          message = message.split('-')
          connection.accept
          connection.send(message[1].encode())



      else:
        # если нет сообщений - удаляем из очереди
        # сокетов, готовых принять сообщение
        outputs.remove(connection)

    # список EXCEPTS - сокеты, в которых произошла ошибка
    for connection in excepts:
      print('Клиент отвалился...')
      # удаляем сокет с ошибкой из всех очередей
      inputs.remove(connection)
      if connection in outputs:
        outputs.remove(connection)
      # закрываем сокет как положено, тем
      # самым очищаем используемые ресурсы
      connection.close()
      # удаляем сообщения для данного сокета
      del messages[connection]

"""
 while True:
  try:
    client, address = server_socket.accept()
    client.setblocking(False)
  except socket.error:
    print(">>> CLIENT NOT FOUND!")
    #time.sleep(10)
  except KeyboardInterrupt:
    print("ERR")
    server_socket.close()
    break
  else:

    r, w, x = select.select(rlist, wlist, xlist[, timeout])

    #main_menu(server_socket)
    result = client.recv(1024)
    #client.send(b"Done!")
    #client.close()
    print("Message: ", result.decode("utf-8"), address)


"""



    #while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        #data = conn.recv(1024).decode()
        #if not data:
        #    # if data is not received break
        #    break
        #print("from connected user: " + str(data))
        #data = input(' -> ')
        #conn.send(data.encode())  # send data to the client

        #conn.close()  # close the connection


if __name__ == '__main__':
    server_program()