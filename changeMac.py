import subprocess
import random
from time import sleep
import netifaces

def check():
    flag = input('Sure? y/n: ')
    if flag == 'y' or flag == 'yes':
        return True
    elif flag == 'no' or flag == 'n':
        print('ok')
        exit()
    else:
        print('Check input')
        exit()

def get_mac():
    mac1 = [random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac1))

print('0%')
sleep(1)
print('2%')
sleep(3)
print('12%')
sleep(0.02)
print('70%')
sleep(1)
print('100%')
listNetworks = netifaces.interfaces()
while True:
    if check() is True:
        for i in listNetworks:
            try:
                mac = get_mac()
                subprocess.call(['ifconfig', i, 'down'])
                subprocess.call(['ifconfig', i, 'hw', 'ether', mac])
                subprocess.call(['ifconfig', i, 'up'])
                print('======================')
                print('MAC address has been changed!')
                print(f"Your mac address for the network {i}: {mac}")
                print('======================')
            except:
                print(f"For the network {i} error caused")
                continue