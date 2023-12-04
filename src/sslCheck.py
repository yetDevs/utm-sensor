import requests
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ssl_cert", type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

def get_ssl_cert_status(ssl_cert, url_file):
    df_list = []
    for url in url_file:
        url = url.strip()  # Remove any leading/trailing whitespace
        try:
            # Try connecting without SSL certificate
            requests.get(url, timeout=5, verify=False)
            df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Fail']}))
        except Exception:
            pass

        try:
            # Try connecting with SSL certificate
            requests.get(url, timeout=5, verify=ssl_cert)
            df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Pass']}))
        except Exception:
            df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Fail']}))

    df = pd.concat(df_list, ignore_index=True)
    return df