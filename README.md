# utm-sensor

All Files output Pandas dataframe from functions.
You're able to import these and utilize the dataframes to output graphics.

# portScan.py

usage: portScan.py [-h] [--server SERVER] [--ports PORTS]

Port Scanner

options:
  -h, --help       show this help message and exit
  --server SERVER  Server IP or URL
  --ports PORTS    Port range to scan

# malUrl.py

usage: malUrl.py [-h] --url-file URL_FILE

options:
  -h, --help           show this help message and exit
  --url-file URL_FILE

# geoIP.py

usage: geoIP.py [-h] --ip-file IP_FILE

options:
  -h, --help         show this help message and exit
  --ip-file IP_FILE

# malDownload

usage: malDownload.py [-h] --mal_url MAL_URL

options:
  -h, --help         show this help message and exit
  --mal_url MAL_URL

# dnsCheck

usage: dnsCheck.py [-h] --domain-file DOMAIN_FILE

options:
  -h, --help            show this help message and exit
  --domain-file DOMAIN_FILE

# dataSense

usage: dataSense.py [-h] --req_data REQ_DATA

options:
  -h, --help           show this help message and exit
  --req_data REQ_DATA I've added req data to /txt/testdata.json
