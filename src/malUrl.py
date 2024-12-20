import argparse
import requests
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url-file", type=argparse.FileType('r'), required=True)
    args = parser.parse_args()
    return args

def malCheck(url_file):
    df_list = []
    for url in url_file:
        url = "http://" + url.strip()  # Remove any leading/trailing whitespace
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                df_list.append(pd.DataFrame({'URL': [url], 'Status': ['Fail']}))
            elif response.status_code == 403:
                df_list.append(pd.DataFrame({'URL': [url], 'Status': ['Pass']}))
            else:
                df_list.append(pd.DataFrame({'URL': [url], 'Status': ['Unknown']}))
        except requests.exceptions.RequestException as e:
            df_list.append(pd.DataFrame({'URL': [url], 'Status': ['Error: ' + str(e)]}))
    df = pd.concat(df_list, ignore_index=True)
    return df

def main():
    args = parse_args()
    df = malCheck(args.url_file)
    print(df)

if __name__ == "__main__":
    main()