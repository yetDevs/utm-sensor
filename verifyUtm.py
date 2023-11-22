import argparse
import socket
import requests
import os
import pandas as pd

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="UTM Effectiveness Testing Tool")
    parser.add_argument('--server', type=str, help='Server to test open ports against')
    parser.add_argument('--port_range', type=lambda x: range(int(x.split('-')[0]), int(x.split('-')[1]) + 1), help='Range of ports to test (e.g., 80-100)')
    parser.add_argument('--malUrl', type=str, help='File path to a list of malicious URLs')
    parser.add_argument('--geoip_file', type=str, help='File path to a list of GEO IPs')
    parser.add_argument('--personal_info_url', type=str, help='URL to send personal info to for testing')
    parser.add_argument('--personal_info', type=str, help='Dummy personal info to test with')
    return parser.parse_args()

def test_open_ports(server, port_range):
    """Test which ports are open."""
    open_ports = []
    for port in port_range:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((server, port))
                open_ports.append(port)
        except:
            pass
    return open_ports

def test_malicious_url_access(file_path):
    """Test if UTM blocks access to malicious URLs."""
    blocked_urls = []
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file]
        for url in urls:
            try:
                response = requests.get(url, timeout=3)
                if response.status_code != 200:
                    blocked_urls.append(url)
            except requests.RequestException:
                blocked_urls.append(url)
                print (response.status_code)
    return blocked_urls

def test_geoip_blocking(file_path):
    """Test if UTM block access to GEO IPs."""
    blocked_ips = []
    with open(file_path, 'r') as file:
        ips = [line.strip() for line in file]
        for ip in ips:
            response = os.system(f"ping -c 1 {ip}")
            if response != 0:
                blocked_ips.append(ip)
    return blocked_ips

def test_personal_info_detection(url, personal_info):
    """Test if UTM detects personal info."""
    try:
        response = requests.post(url, data={'info': personal_info})
        if response.status_code == 200:
            return False  # Not blocked
        else:
            return True   # Blocked
    except requests.RequestException:
        return True       # Assume blocked if there's an exception

def main():
    args = parse_args()

    if args.server and args.port_range:
        open_ports = test_open_ports(args.server, args.port_range)
        print("Open ports:", open_ports)

    if args.malUrl:
        blocked_urls = test_malicious_url_access(args.malUrl)
        print("Blocked malicious URLs:", blocked_urls)

    if args.geoip_file:
        blocked_ips = test_geoip_blocking(args.geoip_file)
        print("Blocked GEO IPs:", blocked_ips)

    if args.personal_info_url and args.personal_info:
        personal_info_blocked = test_personal_info_detection(args.personal_info_url, args.personal_info)
        print("Personal info transmission blocked:", personal_info_blocked)

if __name__ == "__main__":
    main()