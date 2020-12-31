import socket
from IpFinder_Packges import IpFinder

nome_pc = socket.gethostname()
IpFinder(nome_pc)
