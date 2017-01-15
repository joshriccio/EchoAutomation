import smbus
import time
import os
import math

# Class to generate acceleromter readings
class Accelerometer():
    bus = smbus.SMBus(1)
    def __init__(self):
        self.bus.write_byte_data(0x4c, 0x07, 0x00) #Init reg0
        self.bus.write_byte_data(0x4c, 0x08, 0x00) #Calibrate reg0
        self.bus.write_byte_data(0x4c, 0x07, 0x01) #Calibrate reg1
        self.bus.write_byte_data(0x4c, 0x06, 0x10) #Calibrate reg2
    def getValueX(self):
        return self.bus.read_byte_data(0x4c, 0x00)
    def getValueY(self):
        return self.bus.read_byte_data(0x4c, 0x01)
    def getValueZ(self):
        return self.bus.read_byte_data(0x4c, 0x02)

acc = Accelerometer()

for a in range(1000):
    x = acc.getValueX()
    y = acc.getValueY()
    z = acc.getValueZ()
    print("X=", x)
    print("Y=", y)
    print("Z=", z)
    time.sleep(0.2)
    os.system("clear")
