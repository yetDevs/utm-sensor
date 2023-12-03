from src import dataSense, geoIP, dnsCheck, malUrl, portScan, malDownload

# Path: utm-sensor.py

print("Running DNS Check...")
df = dnsCheck.nslookup(open('./txt/domains.txt', 'r'))

print(df)

