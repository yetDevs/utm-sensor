import argparse
import socket
import pandas as pd

def portRanger(portRange: str):
    start, end = map(int, portRange.split('-'))
    return list(range(start, end + 1))

def parse_args():
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('--server', type=str, help='Server IP or URL')
    parser.add_argument('--portRange', type=portRanger, help='Port range to scan')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--output', type=str, help='Output file name')     
    
    return parser.parse_args()

def portCheck(server, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((server, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports



def main():
    args = parse_args()

    if args.server and args.portRange:
        open_ports = portCheck(args.server, args.portRange)
        print(open_ports)

if __name__ == "__main__":
    main()




