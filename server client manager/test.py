import os

def remove_file(filename):
  try:
    os.remove(f'C:\\ProgramData\\{filename}')
  except:
    #client_socket.sendto(f'[*] Error removing {filename}!'.encode(), server)
    print('Error')
  pass

remove_file('Screen')