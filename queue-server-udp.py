import socket
import queue
import re
from tokenize import group

host = 'localhost'
port = 11451

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	s.bind((host, port))
	while True:
		data, addr = s.recvfrom(1024)
		print(f"{addr} => {data}")
		s.sendto(data, addr)

class QueueServer(object):

	def __init__(self, host, port, block_size, regex):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock = s.bind((host, port))
		self.buf = ""
		self.block_size = block_size
		self.queue = queue.Queue()
		# self.regex = regex
		self.group_regex = r"\^([^;\^\$])+\$"
		self.indiv_regex = r"(\d*\.\d+);?"

	def pop(self):
		while self.queue.empty():
			self.parse_buf()
		return self.queue.get()

	def parse_buf(self):
		with re.search(self.group_regex, self.buf) as data_group_match:
			start, end = data_group_match.span()
			self.buf = self.buf[end:]
			group_string = data_group_match.string()
			data_list = re.findall(self.indiv_regex, group_string)
			self.queue.put(data_list)