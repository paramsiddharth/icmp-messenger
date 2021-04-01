from sys import stderr
import socket
from pythonping import ping

MAX_ICMP_PACKET_SIZE = 1508
PAYLOAD_SIZE = MAX_ICMP_PACKET_SIZE // 3

address = input('IP Address: ')

try:
	address = socket.gethostbyname(address)
except socket.gaierror:
	print('Invalid address!', file=stderr)

try:
	while True:
		msg = input('> ')
		while len(msg) > 0:
			if len(msg) > PAYLOAD_SIZE:
				ping(address, count=1, size=PAYLOAD_SIZE, payload=msg[:PAYLOAD_SIZE].encode() + b'\x00')
			else:
				ping(address, count=1, size=PAYLOAD_SIZE, payload=msg[:PAYLOAD_SIZE].encode())
			msg = msg[PAYLOAD_SIZE:]
except KeyboardInterrupt:
	print('Exiting...')