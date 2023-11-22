import argparse
import socket
import requests
import os
import pandas as pd

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="UTM Effectiveness Testing Tool")

    parser.add_argument('--test_open_ports', action='store_true', help='Test open ports (Inside - Out)')
    parser.add_argument('--server', type=str, help='Server to test open ports against')
    parser.add_argument('--port_range', type=lambda x: range(int(x.split('-')[0]), int(x.split('-')[1]) + 1), help='Range of ports to test (e.g., 80-100)')

def portCheck(server, portrange):
    print('test')


def main():
    args = parse_args()

    if args.server and args.port_range:
        open_ports = portCheck(args.server, args.port-range)
        print(open_ports)

if __name__ == "__main__":
    main()




