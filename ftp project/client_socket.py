import socket
def client_socket():
    print('Для выхода из чата наберите: `exit`, `quit` или `q`.')
    # Удаленный хост
    HOST = socket.gethostname()
    # тот же порт, что и у сервера
    PORT = 8000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            mess = input('\nВведите что нибудь >>> ')
            if any(mess.lower() in ext for ext in ['quit', 'exit', 'q']):
                break
            mess = mess.encode('utf-8')
            s.sendall(mess)
            data = s.recv(1024)
            print('\nПолучено: ', data.decode('utf-8'))
"""
def client_program():
    host =  socket.gethostname() #'143.244.145.116'  # as both code is running on same pc
    print(host)
    port = 8000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

"""
if __name__ == '__main__':
    client_socket()