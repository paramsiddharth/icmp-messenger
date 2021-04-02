# Receives ICMP Echo Requests with custom payload

from pprint import pp
import socket
import signal
from os import name as osname

MAX_ICMP_PACKET_SIZE = 1508

signal.signal(signal.SIGINT, lambda *args: (
	print('Exiting...'),
	exit(0)
))

messages = {}

try:
	with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
		s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
		s.bind((socket.gethostname(), 0)) if osname == 'nt' else None

		print('Listening for messages.')

		final_msg = ''
		while True:
			pkt, (ip, port) = s.recvfrom(MAX_ICMP_PACKET_SIZE)

			if ip not in messages.keys():
				messages[ip] = []

			msg_box = messages[ip]

			payload = pkt

			done = True
			if payload[-1] == 0:
				done = False
				payload = payload[:-1]

			msg = payload[
				1 + payload.rfind(b'\x00'):
			].decode('utf-8')

			final_msg += msg

			if done:
				msg_box.append(final_msg)
				print(f'{ip}: {final_msg}')
				final_msg = ''

except KeyboardInterrupt:
	print('Exiting...')