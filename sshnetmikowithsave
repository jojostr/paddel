#Hier soll dann auch mal was in einen File geschrieben werden.

import netmiko
from netmiko import ConnectHandler
import datetime
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.178.25',
    'username': 'josef',
    'password': 'josef',
    'secret': 'cisco',
}

net_connect =ConnectHandler(**iosv_l2)
net_connect.enable()


#Discover the hostname from the running config
hostname = net_connect.send_command('show run | include host')
#hier zeigt er noch die ganze zeile an:
print(hostname)
hostname.split(" ")
hostname,device = hostname.split(" ")
print ("Backing up " + device)
filename = device + '.txt'
showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")   # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

# Finally close the connection, kann ja nicht schaden
# net_connect.disconnect()