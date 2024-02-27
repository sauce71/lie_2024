import machine
import time
from ags10 import AGS10

# Setter opp i2c med en frekvens på 10khz
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=10000)


sensor = AGS10(i2c) # Instans av sensoren


while True:
    tvoc = sensor.total_volatile_organic_compounds_ppb # Leser tvoc
    time.sleep(2) # Må sove litt mellom hver lesing
    resistance = sensor.resistance_kohm # Leser motstand
    time.sleep(2)
    print('TVOC:', tvoc, 'Resistance:', resistance) # Skriver ut de avleste verdiene