import time
import smbus

"""
command to find adress of your connected device: sudo i2cdetect -y 1

somewhrere i saw also this way to assing adress: address = int("8x30",0)

"""
address = 0x38

i2cbus = smbus.SMBus(1)
time.sleep(0.5)

data = i2cbus.read_i2c_block_data(address, 0x71,1)
if (data[0] | 0x08) == 0:
	print("Initialization error")

i2cbus.write_i2c_block_data(address, 0xac, [0x33, 0x00])
time.sleep(0.1)

data = i2cbus.read_i2c_block_data(address, 0x71, 7)

Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
temperature = 200*float(Traw)/2**20 - 50

Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
humidity = 100 * float(Hraw)/2**20

print(round(temperature, 1))
print(round(humidity,1)) 
