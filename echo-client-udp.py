import socket

host = 'localhost'
port = 11451

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	s.sendto(b"hello", (host, port))
	data, addr = s.recvfrom(1024)
	print(f"{addr} => {data}")