# Development-stage entry file after assignment is given
import port_scanner
from unittest import main

# Called with URL
ports = port_scanner.get_open_ports("www.freecodecamp.org", [75,85])
print("Open ports:", ports)

# Called with IP address
ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090])
print("Open ports:", ports)

# Verbose is called with ip address and no host name returned -- single open port
ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
print(ports, '\n')

# Verbose is called with ip address and valid host name returned -- single open port
ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
print(ports, '\n')

# Verbose is called with host name -- multiple ports returned
ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
print(ports, '\n')

# Running unit tests automatically
main(module='test_module', exit=False)