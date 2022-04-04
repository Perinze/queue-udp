import socket
import queue
import re
import select

host = 'localhost'
port = 11451

class QueueServer(object):

	def __init__(self, host, port, tmp_size=1024):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((host, port))
		# self.sock.setblocking(False)
		# self.epoll = select.epoll()
		# self.epoll.register(self.sock.fileno(), select.EPOLLIN)

		self.buf = ''
		self.TMP_SIZE = tmp_size
		self.queue = queue.Queue()

		self.regex = r"\^([\d,]+)\$"
		self.delim = r","

	def pop(self):
		while self.queue.empty():	# is loop safe?
			self.parse_buf()
		return self.queue.get()

	def parse_buf(self):
		self.recv()
		while True:
			match = re.search(self.regex, self.buf)
			if not match:
				break
			_, end = match.span()
			self.buf = self.buf[end:]
			substr = match.group(1)
			data = list(map(int, re.split(self.delim, substr)))
			self.queue.put(data)

	def recv(self):
		tmp, _ = self.sock.recvfrom(self.TMP_SIZE)
		self.buf = ''.join([self.buf, bytes.decode(tmp)])

if __name__ == '__main__':
	qs = QueueServer(host, port)
	print(qs.pop())