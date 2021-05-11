import socket
import sys
import multiprocessing

def scanHost(ip, startPort, endPort):
    print(f'Start TCP port scan {ip}')
    tcp_scan(ip, startPort, endPort)

def tcp_scan(ip, startPort, endPort):
    res = list()
    for port in range(startPort, endPort + 1):
        new_connection = multiprocessing.Process(target=scan_port, args=(ip, port))
        res.append(new_connection)
        new_connection.start()
    for connect in res:
        connect.join()

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((ip, port))
            print(f'TCP PORT : {port} is open.')
            sock.close()
        except:
            pass

if __name__ == '__main__':
    ip = sys.argv[1]
    startPort = int(sys.argv[2])
    endPort = int(sys.argv[3])
    scanHost(ip, startPort, endPort)