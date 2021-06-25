import socket, sys, getopt

#command argument format:

    #scan port 0-1024:
    #python portscan.py www.google.com

    #or scan single:
    #python portscan.py www.google.com 80

    #or scan range:
    #python portscan.py www.google.com 80:100

#14 common network ports from https://opensource.com/article/18/10/common-network-ports

port_app = {
    '20' : 'FTP data',
    '21' : 'FTP control',
    '22' : 'SSH',
    '23' : 'Telnet',
    '25' : 'SMTP',
    '53' : 'DNS',
    '80' : 'HTTP',
    '110' : 'POP3',
    '119' : 'NNTP',
    '123' : 'NTP',
    '143' : 'IMAP',
    '161' : 'SNMP',
    '194' : 'IRC',
    '443' : 'HTTPS'
}

def test_single(ip, port):

    print("scanning port %d on %s" %(port, ip))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    port_avail = s.connect_ex((ip, port))
    s.close()
    
    if(port_avail == 0):
        try:
            print("port %d open - %s" %(port, port_app[str(port)]))
        except:
            print("port %d open" %port)
    else:
        print ("port %d closed" %port)

def test_range (ip, rlo, rhi):

    print("scanning ports %d to %d on %s" %(rlo, rhi, ip))

    for port in range (rlo, rhi+1):
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        port_avail = s.connect_ex((ip, port))
        s.close()
    
        if(port_avail == 0):
            try:
                print("port %d open - %s" %(port, port_app[str(port)]))
            except:
                print("port %d open" %port)

#begin

#test for argv[1]
try:
    #if argv[1] exists
    ip = sys.argv[1]
    argv1 = True
except:
    #if argv[1] dne
    print("please enter an ip address!")
    argv1 = False

#test for argv[2]
try:
    #if argv[2] exists
    port = sys.argv[2]
    argv2 = True
except:
    #if argv[2] dne
    argv2 = False

#test for range or single port
try:
    #if there is a range detected
    port_range = port.split(":")
    rlo = port_range[0]
    rhi = port_range[1]
    range_select = True
except:
    #if there is no range detected
    range_select = False

if((argv1 == True) and (argv2 == False)):

    test_range(ip, 0, 1024)

elif((argv1 == True) and (argv2 == True)):

    if(range_select == True):
        test_range(ip, int(rlo), int(rhi))
    else:
        test_single(ip, int(port))
