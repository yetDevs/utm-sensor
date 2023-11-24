import requests
import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mal_url", type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    return args

def get_mal_urls(mal_url):
    df = pd.DataFrame(columns=['URL', 'Status'])
    for url in mal_url:
        url = url.strip()
        try:
            requests.get(url, timeout=5)
            df = df.append({'URL': url, 'Status': 'Fail'}, ignore_index=True)
        except Exception:
            df = df.append({'URL': url, 'Status': 'Pass'}, ignore_index=True)
    return df

def main():
    args = parse_args()
    df = get_mal_urls(args.mal_url)
    print(df)