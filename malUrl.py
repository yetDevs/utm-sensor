import requests
import pandas as pd
import argparse

def process_urls():
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--url-file", type=argparse.FileType('r'), required=True)
    args = parser.parse_args()

    def malCheck(url_file):
        # Create DataFrame
        df = pd.DataFrame(columns=['URL', 'Status Code'])
        for url in url_file:
            url = url.strip()  # Remove any leading/trailing whitespace
            try:
                response = requests.get(url, timeout=5)
                df = df.append({'URL': url, 'Status Code': response.status_code}, ignore_index=True)
            except requests.exceptions.RequestException as e:
                df = df.append({'URL': url, 'Status Code': 'Error: ' + str('Timeout')}, ignore_index=True)
        return df

    return malCheck(args.url_file)

df = process_urls()
print(df)