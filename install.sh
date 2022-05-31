#!/bin/bash
### initial TrafficLightPi setup script

# update & install needed software
sudo apt update
sudo apt install -y git python3-pip
sudo pip3 install -y ping3

# download script to home directory and make executable
cd ~/
sudo git clone https://github.com/ghostbusker/TrafficLightPi/TrafficLightPi.py
sudo chmod +x TrafficLightPi.py

# create systemd service file
sudo touch /lib/systemd/system/trafficlittle.service
cat <<EOF >> /lib/systemd/system/trafficlittle.service                        
[Unit]
Description=run trafficlittle.py at startup
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/trafficlittle.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
EOF

# update and enable service
sudo systemctl daemon-reload
sudo systemctl enable  trafficlittle.service
sudo systemctl start  trafficlittle.service
exit
