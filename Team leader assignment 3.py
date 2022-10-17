'''Blinking LED'''



import time
import RPi.GPIO as GPIO
GPIO.setmode(11,GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while True:
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(11,False)
    time.sleep(1)




'''Traffic Light'''

import RPi.GPIO as GPIO
from gpiozero import Button, TrafficLights
from time import sleep


button = Button(21)
lights = TrafficLights( 25, 8, 7)


while True:
    button.wait_for_press()
    light.green.on()
    sleep(1)
    lights.off()
    lights.amber.on()
    sleep(1)
    lights.off()
    lights.red.on()
    sleep(1)
    lights.off()
 
