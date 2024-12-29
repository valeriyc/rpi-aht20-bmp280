
Raspberry pi with aht20+bmp280 sensor and data output in prometheus with visualization by grafana.

## Installation

1. Setup Raspberry PI 5 with using PI Imager - choose Other - Raspberry PI OS Lite (64 bit).

2. Connect sensors to Raspberry PI using this tutorial https://www.youtube.com/watch?v=apV93MXHwkA

3. Run `sudo i2cdetect -y 1` to see bmp280 i2c address (should be 76 or 77). Update read-temp.py - address variable if needed.  

4. Install docker-compose, configure docker group:
```
sudo apt update & apt upgrade
sudo apt install docker-compose
sudo groupadd docker
```

5. Run scaap, prometheus and grafana with docker-compose:
```
docker-compose up
```

6. Verify Prometheus config - `<your rpi host name>.local:9090/targets` URL should display `http://scaap:3030/script/temperature` with State="Up"   

7. Configure Grafana.

7.1. Login to http://<your rpi host name>.local:3000/ (change default creds admin/admin)

7.2. Connections - Data Sources - add new Data Source:
- name: Prometheus
- url: http://prometheus:9090/
- Click "Save & Test"

7.3. Dashboards - New Dashboard - Import Dashboard - 
- name: Weather Station
- json: copy-paste content from this URL: https://gist.github.com/ecyshor/d97d520fbfb161a9f7c7370528ed9c87
- select "Prometheus" data source.
