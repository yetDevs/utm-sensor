import socket
import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip-file", type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

def connect_ip(ip_file):
    df_list = []
    for ip in ip_file:
        ip = ip.strip()  # Remove any leading/trailing whitespace
        try:
            socket.create_connection((ip, 80), timeout=5)
            df_list.append(pd.DataFrame({'IP': [ip], 'Status': ['Fail']}))
        except Exception:
            df_list.append(pd.DataFrame({'IP': [ip], 'Status': ['Pass']}))
    df = pd.concat(df_list, ignore_index=True)
    return df

def main():
    args = parse_args()
    df = connect_ip(args.ip_file)
    print(df)

if __name__ == "__main__":
    main()