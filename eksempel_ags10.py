import machine
import time
from ags10 import AGS10
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=10000)

sensor = AGS10(i2c)


while True:
    tvoc = sensor.total_volatile_organic_compounds_ppb
    time.sleep(2)
    resistance = sensor.resistance_kohm
    time.sleep(2)
    print('TVOC:', tvoc, 'Resistance:', resistance)