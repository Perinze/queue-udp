import socket

host = 'localhost'
port = 11451

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((host, port))
	s.sendall(b"hello")
	data = s.recv(1024)

print(f"received {data!r}")