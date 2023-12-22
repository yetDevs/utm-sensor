import argparse
import requests
import pandas as pd
import json

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--req_data", type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

def get_response(req_data_file):
    req_url = 'https://enqeqqyg157lb.x.pipedream.net' #Change this to your own URL
    req_data = json.load(req_data_file)
    response = requests.post(req_url, json=req_data)
    if response.status_code == 200:
        status = 'Fail'
    elif response.status_code == 403:
        status = 'Pass'
    else:
        status = 'Unknown'
    df = pd.DataFrame({'URL': [req_url], 'Status Code': [response.status_code], 'Status': [status]})
    return df

def main():
    args = parse_args()
    df = get_response(args.req_data)
    print(df)

if __name__ == "__main__":
    main()