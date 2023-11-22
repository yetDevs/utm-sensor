import socket
import argparse
import pandas as pd

def process_ips():
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip-file", type=argparse.FileType('r'), required=True)
    args = parser.parse_args()

    def connectIp(ip_file):
        # Create DataFrame
        df = pd.DataFrame(columns=['IP', 'Status'])
        for ip in ip_file:
            ip = ip.strip()  # Remove any leading/trailing whitespace
            try:
                socket.create_connection((ip, '80'), timeout=5)
                df_new = pd.DataFrame({'IP': [ip], 'Status': ['Fail']})
            except Exception:
                df_new = pd.DataFrame({'IP': [ip], 'Status': ['Pass']})
            df = pd.concat([df, df_new], ignore_index=True)
        return df

    return connectIp(args.ip_file)


df = process_ips()
print(df)