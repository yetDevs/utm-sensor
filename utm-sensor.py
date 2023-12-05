import pandas as pd
import argparse
from src import dataSense, geoIP, dnsCheck, malUrl, portScan, malDownload, dmarcCheck

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action='store_true')
    parser.add_argument("--portScan", action='store_true')
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

def main():
    args = parse_args()
    if args.run:
        df = run_tests()
        df.to_csv('output.csv', index=False)
    elif args.portScan:
        df = run_portScan()
        df.to_csv('output.csv', index=False)
    else:
        print("No arguments provided. Please run with --all or --portScan")

if __name__ == "__main__":
    main()


