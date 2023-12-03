import requests
import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mal_url", type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

def get_mal_url_status(mal_url):
    df = pd.DataFrame(columns=['URL', 'Status'])
    for mal_url in mal_url:
        mal_url = mal_url.strip()  # Remove any leading/trailing whitespace
        try:
            requests.get(mal_url, timeout=5)
            df = df.append({'URL': mal_url, 'Status': 'Fail'}, ignore_index=True)
        except Exception:
            df = df.append({'URL': mal_url, 'Status': 'Pass'}, ignore_index=True)
    return df

def main():
    args = parse_args()
    df = get_mal_url_status(args.mal_url)
    print(df)

if __name__ == "__main__":
    main()