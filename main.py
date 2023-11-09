import socket
import os
import keyIN

blocked_ips = {}

def check_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((socket.gethostname(), 1234))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(1)
    try:
        print("Connecting")
        msg, addr = s.recvfrom(1024)
        print('checking ip address of', addr[0])
        print(msg.decode('utf-8'))
        return addr[0]
    except socket.timeout:
        print("Connection Failed")
        return None
    
def Block_ip(ip_address):
    print('Blocking %s' % ip_address)
    os.system('iptables -A INPUT -s ' + ip_address + ' -j DROP')
    blocked_ips[ip_address] = True

while True:
    ip_address = check_ip()
    if ip_address and ip_address in blocked_ips:
        Block_ip(ip_address)
    if keyIN.GetKey(keyIN.CLOSE):
        print('Exiting...')
        exit(1)