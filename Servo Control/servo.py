import RPi.GPIO as GPIO
import time

#Global Pin Variable
pin = None

def askPin():
    validateInput = False
    while not validateInput:
        try:
            a = int(input("Please tell me the pin the servo is connected to: "))
            validateInput = True
        except:
            validateInput = False    
    return a

def askPosition():
    validateInput = False
    while not validateInput:
        try:
            a = float(input("Please tell to which position you want to move the servo [2.5<= position <= 12.5: "))
            if a>=2.5 or a<=12.5:
                validateInput = True
            else:
                validateInput = False
        except KeyboardInterrupt:
            stopServo()
        except:
            validateInput = False    
    return a

def askSpeed():
    speed = ''
    speed = input("Please tell me how fast should the servo move [fast,slow or medium]: ")
    while speed!='fast' or speed!='slow' or speed!='medium':
        speed = input("Give me the speed againg. Hint it can only be fast, slow or medium: ")
    if speed == 'fast':
        sleep = 0.1 
    elif speed == 'medium':
        sleep = 0.5
    else:
        sleep = 0.1
    return sleep

def startServo():
    global pin
    servoPIN = askPin()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    pin = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz this is usually the case for servos
    pin.start(2.5) # Initialization


def stopServo():
    #global pin
    pin.stop()
    GPIO.cleanup()

#def moveClock(currentPosition, speed):
   
#def moveCClock(currentPostiion, speed):

def movePosition(position):
    #global pin
    pin.ChangeDutyCycle(position)
    

try:
    startServo()
    while True:
        pos = askPosition()
        movePosition(pos)
except KeyboardInterrupt:
    stopServo()