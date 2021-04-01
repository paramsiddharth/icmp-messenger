import socket
import os
from scapy.all import ICMP, IP, send

icmp = socket.getprotobyname('icmp')

host_address = socket.gethostbyname(socket.gethostname())
# host_address = '172.22.16.1'
custom_port = 4343
socket_address = (host_address, custom_port)

packet = bytes(IP(dst=host_address) / ICMP(id=os.getpid() & 0xFFFF, seq=0) / 'a')

try:
	with socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) as sock:
		sock.setsockopt(socket.SOL_IP, socket.IP_TTL, 64)
		r = sock.sendto(packet, socket_address)
		print(r)
except KeyboardInterrupt:
	print('Done!')