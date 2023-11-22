import socket
import argparse
import pandas as pd

def portRanger(portRange: str):
    start, end = map(int, portRange.split('-'))
    return list(range(start, end + 1))

def parse_args():
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('--server', type=str, help='Server IP or URL')
    parser.add_argument('--ports', type=portRanger, help='Port range to scan') 
    return parser.parse_args()

def portCheck(server, ports):
    df = pd.DataFrame(columns=['Port', 'Status'])
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((server, port))
        if result == 0:
            df = pd.concat([df, pd.DataFrame({'Port': [port], 'Status': ['Open']})], ignore_index=True)
        else:
            df = pd.concat([df, pd.DataFrame({'Port': [port], 'Status': ['Closed']})], ignore_index=True)
        sock.close()
    return df

def main():
    args = parse_args()
    if args.server and args.ports:
        df = portCheck(args.server, args.ports)
        print(df)

if __name__ == "__main__":
    main()