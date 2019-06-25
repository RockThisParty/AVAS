#coding: utf-8
import os
import http.client
import platform
import re
from getmac import get_mac_address
import dosConstructor
import socket
from winreg import *

psystem = platform.system()
prelease = platform.release()
pversion = platform.version()
mac_address_db = []
print(psystem + " - " + prelease + " - " + pversion)

host = input("[*] Enter the host to scan: ")
if host == '':
	host = socket.gethostbyname(socket.gethostname())

print(socket.gethostname())
print(str(host))

choice = input("Do you want to check your ports? Y-yes/n-no: ")

if psystem == "Windows" and (choice == "Y" or choice == "y" or choice == ''):
    #os.system("launch.bat " + str(host))
    if prelease != "10" and prelease != "8.1":
        print("Your system are not deprecated. Please update your OS")
elif psystem == "Linux" and (choice == "Y" or choice == "y" or choice == ''):
    os.system("launch.sh" + host)

with open("open_ports.txt", 'r') as file:
    for item in file:
        print(item)

port_action = input("Do you want to close all your open ports except 80 and 443? [Y=yes/any other letter=no]")
if port_action == "Y" or port_action == "y":
    if psystem == "Windows":
        for port in range(1, 65536):
            if port != 80 and port != 443:
                os.system("close_ports.bat " + str(port))
                print(str(port) + " is closed")
        for port in range(1, 65536):
            if port != 80 and port != 443:
                os.system("iptables -A INPUT -p tcp --dport " + str(port) + " -j DROP")
                print(str(port) + " is closed")

programs_list_choice = input("Do you want to see all your programs? Y-yes/any other letter - no: ")
UNINSTALL_PATH_LIST = [
    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
    r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
]

programs_dict = dict()

for path in UNINSTALL_PATH_LIST:
    with OpenKey(HKEY_LOCAL_MACHINE, path) as key:
        for i in range(QueryInfoKey(key)[0]):
            keyname = EnumKey(key, i)
            subkey = OpenKey(key, keyname)

            try:
                subkey_dict = dict()
                for j in range(QueryInfoKey(subkey)[1]):
                    k, v = EnumValue(subkey, j)[:2]
                    subkey_dict[k] = v

                if 'DisplayName' not in subkey_dict:
                    continue

                name = subkey_dict['DisplayName'].strip()
                if not name:
                    continue

                programs_dict[name] = subkey_dict

            except WindowsError:
                pass

with open("programs.txt", "w") as file:
    for number, name in enumerate(sorted(programs_dict.keys()), 1):
        subkey_dict = programs_dict[name]
        if programs_list_choice == 'Y' or programs_list_choice == 'y':
            print('{}. {}:'.format(number, name))
            print('    {}: {}'.format('DisplayVersion', subkey_dict.get('DisplayVersion', '')))
            print('\n')
        file.write('{}. {}:'.format(number, name))
        file.write('    {}: {}'.format('DisplayVersion', subkey_dict.get('DisplayVersion', '')))
        file.write('\n')
		
gc = 'Google Chrome'
o = 'Opera'
y = 'Yandex'
f = 'Firefox'
file=open('programs.txt','r')
text=file.read()
print("\nYour browser is:")
if gc in text:
    os.system('findstr /C:' + '"' + gc + '"' + ' programs.txt')
elif o in text:
    print(o)
elif y in text:
    print(y)
elif f in text:
    print(f)
print('')

os_action = input("Want to test your system for popular vulnerabilities? [Y=yes/any other letter=no]")
if os_action == "Y" or os_action =="y":
    print("For your own risk")
    if psystem == "Windows":
        if prelease == "10":
            dosConstructor.dos_1()
            os.system("python dos.py")
            dosConstructor.dos_4()
            os.system("python dos.py")
            dosConstructor.dos_6()
            os.system("dos.js")
        elif prelease == "8" or prelease == "8.1":
            dosConstructor.dos_7()
            os.system("dos.js")
        elif prelease == "7":
            dosConstructor.dos_3()
            os.system("python dos.py")
            dosConstructor.dos_5()
            os.system("dos.js")
            dosConstructor.dos_6()
            os.system("dos.js")
        elif prelease == "Vista":
            dosConstructor.dos_7()
            os.system("dos.js")
            dosConstructor.dos_8()
            os.system("python dos.py")
        elif prelease == "XP" or prelease == "xp" or prelease == "Xp":
            dosConstructor.dos_7()
            os.system("dos.js")
            dosConstructor.dos_8()
            os.system("python dos.py")
            os.system('\\?\AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
A\
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"')
            dosConstructor.dos_9()
            os.system("python dos.py")

mac_address = get_mac_address(ip="192.168.0.1")[:8].upper().replace(":", "-")

#print(mac_address)

with open("macaddressDB.txt", "r", encoding="utf-8") as mdb:
    for line in mdb:
        if mac_address in line:
            print(line)

