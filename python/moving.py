import sys
import smbus
import time
import os
import math
import datetime
debug="true"
filename='log.txt'
value=0
moved=0
countdown=10
vibration=20
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
def printPos():
    global value
    if value:
        value = 0
        return "IN"
    else:
        value = 1
        return "OUT"
 
   
def writeToFile():
    if debug:
        print("writing to file")
    t = datetime.datetime.now().strftime("%I:%M:%S%p\n")
    _file = open(filename,'a')
    _file.write(printPos() +" "+ t)
    _file.close()

while 1:
    x = acc.getValueX()
    y = acc.getValueY()
    z = acc.getValueZ()
    if  x > vibration:
        if moved == 0:
            writeToFile();
        moved=countdown

    if moved > 0:
        for i in range(moved):
            sys.stdout.write('.')
        moved-=1
    print("\n")

    print("X=", x)
    print("Y=", y)
    print("Z=", z)
    time.sleep(0.2)
    os.system("clear")




