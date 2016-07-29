import time
import RPi.GPIO as GPIO
import math

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)

handle_pin = 4
rotary_dial_pin = 2

GPIO.setup (handle_pin, GPIO.IN,GPIO.PUD_UP)
GPIO.setup (rotary_dial_pin, GPIO.IN,GPIO.PUD_UP)

c = 0
count_time = 0
printed = True

def count(pin):
    global c
    global count_time
    global printed
    printed = False
    c = c + 1
    count_time = time.time()
    #print ("c: " + repr(c))

GPIO.add_event_detect(rotary_dial_pin, GPIO.BOTH, callback=count, bouncetime=5)

while True:
    if (time.time() * 1000 - count_time * 1000) > 100:
    	if not(printed): 
            print int((math.floor(c/2)))
        c = 0
        printed = True
    time.sleep(0.1)

