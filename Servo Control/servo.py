import RPi.GPIO as GPIO
import time

#Global Pin Variable
pin = None
currentPosition = 2.5

def askPin():
    validateInput = False
    while not validateInput:
        try:
            a = int(input("Please tell me the pin the servo is connected to: "))
            validateInput = True
        except KeyboardInterrupt:
            exit()
        except:
            validateInput = False    
    return a

def askPosition():
    validateInput = False
    while not validateInput:
        try:
            a = float(input("Please tell to which position you want to move the servo [3<= position <= 11: "))
            if a>=3 or a<=11:
                validateInput = True
            else:
                validateInput = False
        except KeyboardInterrupt:
            stopServo()
            return
        except:
            validateInput = False    
    return a

def askSpeed():
    speed = ""
    speed = str(input("Please tell me how fast should the servo move [fast, medium or slow]: "))
    while speed!="fast" and speed!="slow" and speed!="medium":
        speed = str(input("Give me the speed again. Hint it can only be fast, medium or slow: "))
    if speed == "fast":
        sleep = 0.025 
    elif speed == "medium":
        sleep = 0.01
    else:
        sleep = 0.005
    return sleep

def askMode():
    mode = ""
    mode = str(input("Please tell the servo mode [position or rotation]: "))
    while mode!="position" and mode!="rotation":
        mode = str(input("Give me the mode again. Hint it can only be position or rotation: "))
    return mode

def askRotation():
    rot = ""
    rot = str(input("Please tell the direction of rotation [cw or ccw]: "))
    
    while rot!="cw" and rot!="ccw":
        try:
            rot = str(input("Give me the mode again. Hint it can only be cw or ccw [ clock wise or counter clock wise: "))
        except KeyboardInterrupt:
            stopServo()
            return
    return rot

def startServo():
    global pin
    servoPIN = askPin()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    pin = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz this is usually the case for servos
    pin.start(currentPosition) # Initialization


def stopServo():
    #global pin
    pin.stop()
    GPIO.cleanup()

def moveCClock(speed):
    global currentPosition
    while currentPosition<=11:
        nextPosition = currentPosition+speed
        movePosition(nextPosition)
        currentPosition = nextPosition
        #time.sleep(0.1)
    return
    
   
def moveClock(speed):
    global currentPosition
    while currentPosition>=3:
        nextPosition = currentPosition-speed
        movePosition(nextPosition)
        currentPosition = nextPosition
        #time.sleep(0.1)
    return

def movePosition(position):
    global currentPosition
    pin.ChangeDutyCycle(position)
    currentPosition = position

def moveSmoothPosition(position,speed):
    global currentPosition

    if position < currentPosition:
        while currentPosition >= position:
            nextPosition = currentPosition-speed
            movePosition(nextPosition)
            currentPosition = nextPosition
        return
    elif position > currentPosition:
            while currentPosition <= position:
                nextPosition = currentPosition+speed
                movePosition(nextPosition)
                currentPosition = nextPosition
            return
    else:
        return


try:
    startServo()
    mode = askMode()
    speed = askSpeed()
    if mode == "position":
        while True:
            pos = askPosition()
            moveSmoothPosition(pos,speed)
    else:
        while True:
            rot = askRotation()
            if rot == "cw":
                moveClock(speed)
            else:
                moveCClock(speed)
except KeyboardInterrupt:
    stopServo()