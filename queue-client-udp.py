import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"hwe^123,234,345,645$498wfh^12,23,34,76$4ewjifd", ("localhost", 11451))
s.close()