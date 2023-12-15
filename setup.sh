#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3 python3-pip git -y
git clone https://github.com/yetDevs/utm-sensor.git
cd utm-sensor
pip3 install -r requirements.txt
echo "Complete."