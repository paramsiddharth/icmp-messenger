from pprint import pp
import socket
from scapy.all import ICMP

MAX_ICMP_PACKET_SIZE = 1508

messages = {}

try:
	with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
		s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)

		print('Listening for messages.')

		while True:
			pkt, (ip, port) = s.recvfrom(MAX_ICMP_PACKET_SIZE)

			if ip not in messages.keys():
				messages[ip] = {
					'idx': 0,
					'data': []
				}

			msg_box = messages[ip]

			payload = ICMP(pkt).load
			msg = payload[
				1 + payload.rfind(b'\x00'):
			].decode('utf-8')

			msg_box['idx'] += 1
			msg_box['data'].append(msg)

			print(f'{ip}: {msg}')
except KeyboardInterrupt:
	print('Exiting...')