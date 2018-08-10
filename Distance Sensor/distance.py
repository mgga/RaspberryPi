#!/usr/bin/env python3
# Author: Miguel Almeida
import time
import math
import RPi.GPIO as GPIO
from subprocess import PIPE, Popen

def get_cpu_temperature():
    #get cpu temperature using vcgencmd#
    try:
        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(tFile.read())
        tempC = temp/1000
        return tempC
    except:
        tFile.close()
        exit()

while True:
    temp = get_cpu_temperature()
    print(temp)
    time.sleep(0.5)