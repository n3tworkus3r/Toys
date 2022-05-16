import socket
from ftplib import FTP

###############################################################
######################### FUNCTIONS ###########################
###############################################################
#                                                             #
#                      ################                       #
#                      ##### MENU #####                       #
#                      ################                       #
#

def main_menu():

  while True:
    print('\n\t\tMENU:\n'
    '[ls-u] - show users\n'
    '[sl] - select user\n')

    key = input('Enter a command: ')
    match key:
      case 'ls-u':
        show_users()
      case 'sl':
        select_user()
  pass

def show_users():

  pass




def user_menu(session):
  while True:
    print('\n\t\tUSER MENU:\n'
    '[ls] - show files\n'
    '[dwn] - download file\n'
    '[dwn-a] - download all files\n'
    '[upl] - upload file\n')

    key = input('Enter a command: ')
    match key:
      case 'help':
        help()
      case 'ls':
        ls(session)
      case 'dwn':
        download(session)
      case 'dwn-a':
        download_all(session)
      case 'upl':
        upload(session)
  pass

def ls(session):
  data = session.retrlines('LIST')
  print(data)
  pass

def download(session):
  file_name = input('Enter a file name: ')
  save_dir = 'D:\\FTP\\' + file_name # Путь, где сохранить файл.
  try:
    session.retrbinary('RETR ' + file_name, open(save_dir + file_name, 'wb').write)
    print('File {0} downloaded succesfully!'.format(file_name))
  except:
    print('ERROR DOWNLOADING FILE: ' + file_name)
  pass

def download_all(session):
  # Get All Files
  files = session.nlst()
  # Print out the files
  for file in files:
    print("Downloading..." + file)
    session.retrbinary("RETR " + file ,open("D:\\" + file, 'wb').write)
  pass

def upload(session):
  print('File will upload from Desktop!')
  filename = input('Enter a filename: ')
  file = open('C:\\Users\\US3R\\Desktop\\{0}'.format(filename), 'rb')  # file to send
  session.storbinary('STOR ' + filename, file)
  print('File {0} was sended'.format(filename))
  pass

def help():
  print('Help yourself!')


"""
###############################################################
######################### EXECUTION ###########################
###############################################################
"""

HOST = socket.gethostname()
# тот же порт, что и у сервера
PORT = 8000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
  try:
    server.connect((HOST, PORT))
    while True:
      print('\n\t\tMANAGER MENU:\n'
            '[cl] - show connection list\n'
            '[sl] - select connection\n')
      key = input('Enter a command: ')
      match key:
        case 'cl':
          server.send('connection list'.encode('utf-8'))

          data = server.recv(1024) # Receive 1024 bytes packet from server
          print('\n',data.decode('utf-8'))
        case 'sl':
          connection_address = input('Enter connection address: ')
          server.send('select connection-{0}'.format(connection_address).encode('utf-8'))

          data = server.recv(1024) # Receive 1024 bytes packet from server
          print('\n', data.decode('utf-8'))

  except:
    print('CONNECT ERROR!!!')



#session = FTP()
#HOST = '143.244.145.116'
#PORT = 2223


#session.connect(HOST, PORT)
#  session.login('Y7V','PSWD')
#  print('Client connected to host {0}'.format(HOST))
#  user_menu(session)








"""


def ftp_upload(ftp_obj, path, ftype='TXT'):

    #Функция для загрузки файлов на FTP-сервер
    #@param ftp_obj: Объект протокола передачи файлов
    #@param path: Путь к файлу для загрузки

    if ftype == 'TXT':
        with open(path) as fobj:
            ftp.storlines('STOR ' + path, fobj)
    else:
        with open(path, 'rb') as fobj:
            ftp.storbinary('STOR ' + path, fobj, 1024)


if __name__ == '__main__':
    #ftp = FTP('127.0.0.1:8000')
    ftp = FTP.connect(self='143.244.145.116:8000', host='', port=8000)
    #ftp.login()

    file_path = 'C:\\Users\\US3R\\Desktop\\upload.txt'
    ftp_upload(ftp, file_path)

    #pdf_path = '/path/to/something.pdf'
    #ftp_upload(ftp, pdf_path, ftype='PDF')

    ftp.quit()

"""















'''
import socket

port = 2000
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',port))

try:
    server.listen(100)
    print('Server listening on port {0}...'.format(port))
except:
 time.sleep(60)


client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')

print(data)
HTTP_header = 'HTTP:/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
content = 'Hello bitch'.encode('utf-8')
client_socket.send(HTTP_header.encode('utf-8') + content)
print('complete...')

'''