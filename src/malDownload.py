import requests
import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mal_url", type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

def get_mal_url_status(mal_url):
    df_list = []
    for mal_url in mal_url:
        mal_url = mal_url.strip()  # Remove any leading/trailing whitespace
        try:
            requests.get(mal_url, timeout=5)
            df_list.append(pd.DataFrame({'URL': [mal_url], 'Status': ['Fail']}))
        except Exception:
            df_list.append(pd.DataFrame({'URL': [mal_url], 'Status': ['Pass']}))
    df = pd.concat(df_list, ignore_index=True)
    return df

def main():
    args = parse_args()
    df = get_mal_url_status(args.mal_url)
    print(df)

if __name__ == "__main__":
    main()