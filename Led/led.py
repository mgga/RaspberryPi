#!/usr/bin/env python3
# Authors: Miguel Almeida, Tony DiCola (tony@tonydicola.com)

import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def colorWipe(strip, color, wait_ms=0):
    #All the LEDs with the same color#
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        if wait_ms != 0:
            time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    #Movie theater light style chaser animation#
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    #Generate rainbow colors across 0-255 positions#
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    #Draw rainbow that fades across all pixels at once#
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    #Draw rainbow that uniformly distributes itself across all pixels#
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    #Rainbow movie theater light style chaser animation#
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def askPin():
    validateInput = False
    while not validateInput:
        try:
            a = int(input("Please tell me the pin the LED strip is connected to: "))
            validateInput = True
        except KeyboardInterrupt:
            cleanLED()
            exit()
        except:
            validateInput = False    
    return a

def askMode():
    mode = ""
    mode = str(input("Please tell the LED mode [color, theater, rainbow]: "))
    while mode!="color" and mode!="theater" and mode!="rainbow":
        mode = str(input("Give me the mode again. Hint it can only be color, theater, rainbow: "))
    return mode

def askColor():
    validateInput = False
    while not validateInput:
        try:
            #list(map(int, input().split()))
            val = list(map(int, input("Please tell me the color you want R G B [give them as numbers between 0 and 255 separated by spaces] ").split()))
            try:
                if val[0]>=0 and val[0]<=255 and val[1]>=0 and val[1]<=255 and val[2]>=0 and val[2]<=255:
                    validateInput = True
            except:
                validateInput = False
        except KeyboardInterrupt:
            cleanLED()
            exit()
        except:
            validateInput = False
    return val

def askIterations():
    validateInput = False
    while not validateInput:
        try:
            a = int(input("Please tell me the number of iterations: "))
            validateInput = True
        except KeyboardInterrupt:
            cleanLED()
            exit()
        except:
            validateInput = False    
    return a

def askRainbow():
    mode = ""
    mode = str(input("Please tell the type of Rainbom you want [normal, cycle, theater]: "))
    while mode!="normal" and mode!="cycle" and mode!="theater":
        mode = str(input("Give me the mode again. Hint it can only be normal, cycle, theater: "))
    return mode

def cleanLED():
    colorWipe(strip, Color(0,0,0), 0)


LED_PIN = askPin()
try:
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
except:
    print("Try running as sudo!")

try:    
    mode = askMode()
    
    if mode == "color":
        while True:
            color = askColor()
            colorWipe(strip, Color(color[0],color[1],color[2]),0)
    elif mode == "theater":
        while True:
            color = askColor()
            times = askIterations()
            theaterChase(strip, Color(color[0],color[1],color[2]),50, times)
    else:
        while True:
            rainbow = askRainbow()
            if rainbow == "normal":
                rainbow(strip)
            elif rainbow == "cycle":
                rainbowCycle(strip)
            else:
                theaterChaseRainbow(strip)
        
except KeyboardInterrupt:
    cleanLED()
    exit()
