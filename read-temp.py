import time

from smbus2 import SMBus
from bmp280 import BMP280

# pip install bmp280

port = 1
address = 0x77

bus = SMBus(port)
bmp280 = BMP280(i2c_addr=address,i2c_dev=bus)

def print_gauge(name, value, text):
    print(f'# HELP {name} {text}')
    print(f'# TYPE {name} gauge')
    print(f'{name} {value}')


# the compensated_reading class has the following attributes
print_gauge("temperature", bmp280.get_temperature(), "Temperature in celsius")
print_gauge("pressure", bmp280.get_pressure(), "Pressure")
print_gauge("humidity", "N/A", "Humidity percentage")

