# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
import time
import RPi.GPIO as GPIO

#Global Pin Variable
pin = None

def askPin():
    validateInput = False
    while not validateInput:
        try:
            a = int(input("Please tell me the pin the rain sensor is connected to: "))
            validateInput = True
        except KeyboardInterrupt:
            exit()
        except:
            validateInput = False    
    return a

def startRain():
    global pin
    pin = askPin()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def readRain():
    rain = GPIO.input(pin) #pin will be high if not wet
    return not rain

def stopRain():
    GPIO.cleanup()

try:
    startRain()
    while True:
        if readRain():
            print("It's raining !")
            time.sleep(1)
except KeyboardInterrupt:
    stopRain()