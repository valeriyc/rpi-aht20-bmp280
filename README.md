
Raspberry PI with AHT20+BMP280 sensor and data output in Prometheus with visualization by Grafana.

## Installation

1. Setup OS on Raspberry PI 5 SD card using PI Imager - choose Other - Raspberry PI OS Lite (64 bit).

2. Connect AHT20+BMP280 sensor to Raspberry PI:

|Pin #|Pin Name|Connection|
|-----|--------|----------|
|1|3.3v|VDO|
|3|GPIO2|SDA|
|5|GPIO3|SCL|
|9|GND|GND|

3. Connect to RPI using SSH, setup docker-compose:
```
sudo apt update & apt upgrade
sudo apt install docker-compose
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
4. Clone this repository, build & run docker containers:
```
cd rpi-aht20-bmp280
docker compose up -d
docker compose logs -f
```
5. Configure Grafana.
    * Login to http://your_host_name.local:3000/ (change default creds admin/admin)
    * Open 'Connections' - 'Data Sources' - add new Data Source:
        * name: Prometheus
        * url: http://prometheus:9090/
        * Click "Save & Test".
          
    * Open 'Dashboards' - 'New Dashboard' - 'Import Dashboard': 
        * name: <dashboard name>
        * json: copy-paste content from this URL: https://gist.github.com/ecyshor/d97d520fbfb161a9f7c7370528ed9c87
        * select "Prometheus" data source.

## Troubleshooting:

1. Verify Prometheus config - `<host name>.local:9090/targets` URL should display `http://scaap:3030/script/temperature` with State="Up"   

2. Run `sudo i2cdetect -y 1` to see bmp280 and aht20 addresses. Update them in read-temp.py if needed.  

3. Run/debug read-temp.py script: 
```
apt-get update && apt-get -y install python3 python3-pip
python3 -m venv .venv
source .venv/bin/activate
pip3 install smbus2 bmp280 
python3 read-temp.py
```
