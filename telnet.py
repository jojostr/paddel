#Ein funktionierendes Programm um sich per telnet auf den Hausswitch zu verbinden und eine loopback Adresse anzulegen
#Aber auch nur mit einem 2er python...
import getpass
import telnetlib

HOST="192.168.178.25"

user = raw_input("Enter your username ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until("Username: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("configure t\n")
tn.write("interface loopback0\n")
tn.write("ip address 1.1.1.1 255.255.255.255 \n")
print (tn.read_all())
#ueberfluessige zeile
