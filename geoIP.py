import socket
import os
import argparse

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