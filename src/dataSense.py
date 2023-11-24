import argparse
import requests
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--req_url", type=str, required=True)
    parser.add_argument("--req_data", type=str, required=True)
    args = parser.parse_args()
    return args

def get_response(req_url, req_data):
    response = requests.post(req_url, data={'info': req_data})
    status = 'Fail' if response.status_code == 200 else 'Pass'
    df = pd.DataFrame({'URL': [req_url], 'Status Code': [response.status_code], 'Status': [status]})
    return df

def main():
    args = parse_args()
    df = get_response(args.req_url, args.req_data)
    print(df)

if __name__ == "__main__":
    main()