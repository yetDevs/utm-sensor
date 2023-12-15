import pandas as pd
import argparse
from src import dataSense, geoIP, dnsCheck, malUrl, portScan, malDownload, dmarcCheck, syncAssets, assetConfig, sslCheck
from src.assetConfig import assets
try:
    import _bootlocale
except ImportError:
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runAll", action='store_true')
    parser.add_argument("--portScan", action='store_true')
    parser.add_argument("--sslCheck", action='store_true')
    parser.add_argument("--syncAssets", type=str)
    args = parser.parse_args()
    return args

def run_tests():
    print("Running Data Sense...")
    df_dataSense = dataSense.get_response(open('./assets/testdata.json', 'r'))
    df_dataSense['Module'] = 'Data Sense'
    print(df_dataSense)

    print("Running DNS Check...")
    df_dnsCheck = dnsCheck.nslookup(open('./assets/domains.txt', 'r'))
    df_dnsCheck['Module'] = 'DNS Check'
    print(df_dnsCheck)

    print("Running GeoIP...")
    df_geoIP = geoIP.connect_ip(open('./assets/ips.txt', 'r'))
    df_geoIP['Module'] = 'GeoIP'
    print(df_geoIP)

    print("Running Malicious URL Check...")
    df_malUrl = malUrl.malCheck(open('./assets/urls.txt', 'r'))
    df_malUrl['Module'] = 'Malicious URL Check'
    print(df_malUrl)

    print("Dmarc Check...")
    df_dmarc = dmarcCheck.check_dmarc(open('./assets/maildomain.txt', 'r'))
    df_dmarc['Module'] = 'DMARC Check'
    print(df_dmarc)

    print("Running Malicious Download Check...")
    df_malDownload = malDownload.get_mal_url_status(open('./assets/malware.txt', 'r'))
    df_malDownload['Module'] = 'Malicious Download Check'
    print(df_malDownload)

    final_df = pd.concat([df_dataSense, df_dnsCheck, df_geoIP, df_malUrl, df_dmarc, df_malDownload], ignore_index=True)  # Add other dataframes to this list
    return final_df

def run_portScan():
    print("Running Port Scan...")
    df_portScan = portScan.portCheck('scanme.nmap.org', portScan.portRanger('20-23'))
    df_portScan['Module'] = 'Port Scan'
    print(df_portScan)

    df_portScan = pd.concat([df_portScan], ignore_index=True)  # Add other dataframes to this list
    return df_portScan

def run_sslCheck():
    print("Running SSL Check...")
    df_sslCheck = sslCheck.get_ssl_cert_status(sslCheck.getCert('./assets/cert.pem'), open('./assets/sslCheckUrls.txt', 'r'))
    df_sslCheck['Module'] = 'SSL Check'
    print(df_sslCheck)

    df_sslCheck = pd.concat([df_sslCheck], ignore_index=True)  # Add other dataframes to this list
    return df_sslCheck

def main():
    args = parse_args()
    if args.runAll:
        df = run_tests()
        df.to_csv('tests_Output.csv', index=False)
    elif args.portScan:
        df = run_portScan()
        df.to_csv('portScan_Output.csv', index=False)
    elif args.sslCheck:
        df = run_sslCheck()
        df.to_csv('sslCheck_Output.csv', index=False)
    elif args.syncAssets:
        syncAssets.syncAssets(assets[args.syncAssets])
    else:
        print("No arguments provided. Please run with --runAll or --portScan or --syncAssets [malUrls/malDomains/ipList]")

if __name__ == "__main__":
    main()


