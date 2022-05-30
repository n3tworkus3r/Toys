from ftplib import FTP


session = FTP()
HOST = '157.245.7.127'
PORT = 60001

try:
    session.connect(HOST, PORT)
    session.login('Y7V','PSWDF')

    print('Client connected to host {0}'.format(HOST))

    #filename = '19.jpg'
    #file = open('C:\\Users\\US3R\\Desktop\\{0}'.format(filename), 'rb')  # file to send
    #session.storbinary('STOR ' + filename, file)
    print('File was sended')
    data = session.retrlines('LIST')
    print(data)

except:
    print('CONNECT ERROR!!!')







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