import argparse
import socket
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain-file", type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    return args

def nslookup(domain_file):
    df = pd.DataFrame(columns=['Domain', 'IP Address'])
    for domain in domain_file:
        domain = domain.strip()  # Remove any leading/trailing whitespace
        try:
            ip_address = socket.gethostbyname(domain)
            df_new = pd.DataFrame({'Domain': [domain], 'IP Address': [ip_address], 'Status': ['Fail']})
        except socket.gaierror:
            df_new = pd.DataFrame({'Domain': [domain], 'IP Address': ['Error: Invalid domain'], 'Status': ['Pass']})
        df = pd.concat([df, df_new], ignore_index=True)
    return df

def main():
    args = parse_args()
    df = nslookup(args.domain_file)
    print(df)

if __name__ == "__main__":
    main()