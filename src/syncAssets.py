import requests
import argparse
import os
from src.assetConfig import assets

def parse_args():
    parser = argparse.ArgumentParser()
    for asset in assets:
        parser.add_argument("--" + asset, action='store_true', help=assets[asset]['help'])
    parser.add_argument("--all", action='store_true', help="Update all assets")
    args = parser.parse_args()
    return args


def syncAssets(testName):
    url = testName['url']
    filename = testName['filename']
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            with open(filename, 'w') as f:
                split = response.text.splitlines()
                split = split[-10:]
                for line in split:
                    f.write(line + '\n')
            print("Successfully updated " + filename)
        else:
            print("Error: " + str(response.status_code))
    except requests.exceptions.RequestException as e:
        print("Error: " + str(e))
    

def main():
    args = parse_args()
    print(assets)
    if args.all:
        for asset in assets['assets']:
            syncAssets(asset)
    elif args.malDomains:
        syncAssets(assets['malDomains'])
    elif args.ipList:
        syncAssets(assets['ipList'])
    elif args.malUrls:
        syncAssets(assets['malUrls'])
    else:
        print("No assets selected. Please use --all or select a specific asset to update.")
        print("Use --help for more information.")
        return

if __name__ == "__main__":
    main()