# Lists host IP addresses on all interfaces

import socket

data = socket.gethostbyname_ex(socket.gethostname())
cname = data[0]
ips = data[2]

print(f'Network Addresses for "{cname}":')
for i in range(len(ips)):
	print(f' {i} - {ips[i]}')