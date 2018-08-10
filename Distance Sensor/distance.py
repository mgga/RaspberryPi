#!/usr/bin/env python3
# Author: Miguel Almeida
import time
import math
import RPi.GPIO as GPIO
from subprocess import PIPE, Popen

def get_cpu_temperature():
    #get cpu temperature using vcgencmd#
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

while True:
    temp = get_cpu_temperature
    print(temp)
    time.sleep(0.5)