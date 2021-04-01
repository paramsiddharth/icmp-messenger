from sys import stderr
import socket
from pythonping import ping

MAX_ICMP_PACKET_SIZE = 1508

address = input('Enter the IP address of the receiver: ')

try:
	address = socket.gethostbyname(address)
except socket.gaierror:
	print('Invalid address!', file=stderr)

msg = 'Hi! How are you?'
pkt_size = (MAX_ICMP_PACKET_SIZE // 3)

try:
	r = ping(address, count=1, size=pkt_size, payload=msg[:pkt_size].encode())
	print(r)
except KeyboardInterrupt:
	print('Exiting...')