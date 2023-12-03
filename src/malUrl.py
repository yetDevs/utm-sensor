import requests
import pandas as pd
import argparse

def process_urls():
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--url-file", type=argparse.FileType('r'))
    args = parser.parse_args()

    def malCheck(url_file):
        # Create DataFrame
        df = pd.DataFrame(columns=['URL', 'Status Code'])
        for url in url_file:
            url = url.strip()  # Remove any leading/trailing whitespace
            try:
                response = requests.get(url, timeout=5)
                df = pd.DataFrame({'URL': [url], 'Status Code': [response.status_code]})
            except requests.exceptions.RequestException as e:
                df = pd.DataFrame({'URL': [url], 'Status Code': ['Error: ' + str('Timeout')]})
            df = pd.concat([df, df], ignore_index=True)
        return df

    return malCheck(args.url_file)

def main():
    df = process_urls()
    print(df)

if __name__ == "__main__":
    main()