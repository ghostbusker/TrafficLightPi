#!/bin/bash
### initial TrafficLightPi setup script

# add log2ram repositories need for apt install, improves SD card stability
echo "deb [signed-by=/usr/share/keyrings/azlux-archive-keyring.gpg] http://packages.azlux.fr/debian/ bullseye main" | sudo tee /etc/apt/sources.list.d/azlux.list
sudo wget -O /usr/share/keyrings/azlux-archive-keyring.gpg  https://azlux.fr/repo.gpg

# update & install needed software
sudo apt update
sudo apt install -y git python3-pip log2ram
sudo pip3 install -y ping3

# download script to home directory and make executable
cd ~/
sudo git clone https://github.com/ghostbusker/TrafficLightPi/TrafficLightPi.py
sudo chmod +x TrafficLightPi.py

# create systemd service file
sudo touch /lib/systemd/system/trafficlightpi.service
cat <<EOF >/lib/systemd/system/trafficlightpi.service                        
[Unit]
Description=run trafficlightpi.py at startup
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/TrafficLightPi.py    ###THIS LINE ASSUMES YOUR USERNAME IS "pi"###
Restart=on-abort

[Install]
WantedBy=multi-user.target
EOF

# update and enable service
sudo systemctl daemon-reload
sudo systemctl enable  trafficlittle.service
sudo systemctl start  trafficlittle.service
exit
