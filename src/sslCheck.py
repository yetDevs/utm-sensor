import requests
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ssl_cert", type=argparse.FileType('r'))
    args = parser.parse_args()
    return args

def getCert(path):
    if not path.endswith('.pem'):
        raise ValueError('Invalid file type. Please provide a .pem file.')
    with open(path, 'r') as f:
        cert = f.read()
    return cert

def get_ssl_cert_status(ssl_cert, url_file):
    df_list = []
    for url in url_file:
        url = url.strip()  # Remove any leading/trailing whitespace
        try:
            # Try connecting without SSL certificate
            req = requests.get(url, timeout=5, verify=False)
            if req.status_code == 200:
                df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Fail']}))
            elif req.status_code == 403:
                df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Pass']}))
            else:
                df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Unknown']}))
        except Exception:
            pass

        try:
            # Try connecting with SSL certificate
            sslReq = requests.get(url, timeout=5, verify=ssl_cert)
            if sslReq.status_code == 200:
                df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Fail']}))
            elif sslReq.status_code == 403:
                df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Pass']}))
            else:
                df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Unknown']}))
        except Exception:
            df_list.append(pd.DataFrame({'URL': [url], 'SSL Status': ['Error']}))

    df = pd.concat(df_list, ignore_index=True)
    return df