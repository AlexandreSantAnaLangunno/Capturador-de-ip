import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('')
print('-------------------------------------' * 2)
print("Nome do Computador: ", hostname)
print('-------------------------------------' * 2)
print('Seu Ip: ', local_ip)
