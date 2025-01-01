import time
import smbus2
from smbus2 import SMBus
from bmp280 import BMP280

# pip3 install smbus2 bmp280

port = 1
addressBMP280 = 0x77
addressAHT20 = 0x38

bus = SMBus(port)
bmp280 = BMP280(i2c_addr=addressBMP280,i2c_dev=bus)


def getHumidity(address, i2cbus):
    #AHT20 code:
    #https://raspberrypi.stackexchange.com/questions/133457/how-can-rpi4b-use-python-to-talk-to-the-i2c-dht20-sht20-temperature-and-humidi 
    time.sleep(0.5)
    data = i2cbus.read_i2c_block_data(address,0x71,1)
    if (data[0] | 0x08) == 0:
       print('Initialization error')
    i2cbus.write_i2c_block_data(address,0xac,[0x33,0x00])
    time.sleep(0.1)
    data = i2cbus.read_i2c_block_data(address,0x71,7)
    Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
    temperature = 200*float(Traw)/2**20 - 50
    Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
    humidity = 100*float(Hraw)/2**20
    return humidity

humidity = getHumidity(addressAHT20, bus)

def print_gauge(name, value, text):
    print(f'# HELP {name} {text}')
    print(f'# TYPE {name} gauge')
    print(f'{name} {value}')


# the compensated_reading class has the following attributes
print_gauge("temperature", bmp280.get_temperature(), "Temperature in celsius")
print_gauge("pressure", bmp280.get_pressure(), "Pressure")
print_gauge("humidity", humidity, "Humidity percentage")

