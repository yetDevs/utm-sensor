import pandas as pd
from src import dataSense, geoIP, dnsCheck, malUrl, portScan, malDownload, dmarcCheck

def run_tests():
    print("Running Data Sense...")
    df_dataSense = dataSense.get_response(open('./txt/testdata.json', 'r'))
    df_dataSense['Module'] = 'Data Sense'
    print(df_dataSense)

    print("Running DNS Check...")
    df_dnsCheck = dnsCheck.nslookup(open('./txt/domains.txt', 'r'))
    df_dnsCheck['Module'] = 'DNS Check'
    print(df_dnsCheck)

    print("Running GeoIP...")
    df_geoIP = geoIP.connect_ip(open('./txt/ips.txt', 'r'))
    df_geoIP['Module'] = 'GeoIP'
    print(df_geoIP)

    print("Running Malicious URL Check...")
    df_malUrl = malUrl.malCheck(open('./txt/urls.txt', 'r'))
    df_malUrl['Module'] = 'Malicious URL Check'
    print(df_malUrl)

    print("Dmarc Check...")
    df_dmarc = dmarcCheck.check_dmarc(open('./txt/maildomain.txt', 'r'))
    df_dmarc['Module'] = 'DMARC Check'
    print(df_dmarc)

    print("Running Malicious Download Check...")
    df_malDownload = malDownload.get_mal_url_status(open('./txt/malware.txt', 'r'))
    df_malDownload['Module'] = 'Malicious Download Check'
    print(df_malDownload)

    print("Running Port Scan...")
    df_portScan = portScan.portScan(open('./txt/scanip.txt', 'r'))
    df_portScan['Module'] = 'Port Scan'
    print(df_portScan)


    final_df = pd.concat([df_dataSense, df_dnsCheck, df_geoIP, df_malUrl, df_dmarc, df_portScan, df_malDownload], ignore_index=True)  # Add other dataframes to this list
    return final_df

df = run_tests()
print(df)