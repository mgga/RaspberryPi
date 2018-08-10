#!/usr/bin/env python3
# Author: Miguel Almeida
import time
import math
import RPi.GPIO as GPIO
from subprocess import PIPE, Popen

#Global Pin Variable
pinTrig = None
pinEcho = None

def askPin(name):
    validateInput = False
    while not validateInput:
        try:
            a = int(input("Please tell me the pin the "+name+" is connected to: "))
            validateInput = True
        except KeyboardInterrupt:
            exit()
        except:
            validateInput = False    
    return a

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

def stopDistance():
    GPIO.cleanup()

def get_air_temperature():
    temp = get_cpu_temperature()
    airtemp = temp-20
    return airtemp

def calcDistanceCM(time):
    speedOfSound = 331.3 * math.sqrt(1 + (get_cpu_temperature()/273.15))
    distance = time * ((speedOfSound*100)/2)
    return distance

def startSensor():
    global pinTrig, pinEcho
    pinTrig = askPin("trigger")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinTrig, GPIO.OUT)
    pinEcho = askPin("echo")
    GPIO.setup(pinEcho, GPIO.IN)
    GPIO.output(pinTrig, GPIO.LOW)

def measureTime():
    GPIO.output(pinTrig, False)
    time.sleep(0.00001)
    GPIO.output(pinTrig, True)
    time.sleep(0.00001)
    GPIO.output(pinTrig, False)
    dropCounter = 0
    drop = False
    while GPIO.input(pinEcho) == 0:
        if dropCounter < 1000:
            timeOff = time.time()
            dropCounter += 1
        else:
            drop = True
            print("Echo not recieved")
            break
    while GPIO.input(pinEcho) == 1:
        timeOn = time.time()
    deltaT = timeOn - timeOff
    return deltaT

try:
    startSensor()
    while True:
        distance = calcDistanceCM(measureTime())
        print("Distance is "+str(distance)+"cm")
        time.sleep(0.01)

except:
    stopDistance()