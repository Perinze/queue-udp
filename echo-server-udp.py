import socket

host = 'localhost'
port = 11451

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	s.bind((host, port))
	while True:
		data, addr = s.recvfrom(1024)
		print(f"{addr} => {data}")
		s.sendto(data, addr)