import socket, re

def get_open_ports(target, port_range, verbose_mode=False):
    ip = ""
    open_ports = []
    try:
        ip = socket.gethostbyname(target)
        for port in range(port_range[0], port_range[1]):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
    except KeyboardInterrupt:
        return("Exiting program!!!")
    except socket.gaierror:
        if(re.search('[a-zA-Z]'), target):
            return("Error: Invalid hostname")
        return("Error: Invalid IP address")
    except socket.error:
        return("Error: Invalid IP address")

    return(open_ports)
  