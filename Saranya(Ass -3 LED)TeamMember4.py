import RPi.GPIO as GPIO
import time

def blink(led):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)
    previous_button_state +=1
    if(previous_button_state > 2):
        previous_button_state = 0

previous_button_state = 0

LED_PIN = [17, 22, 27]
BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN[0], GPIO.OUT)
GPIO.setup(LED_PIN[1], GPIO.OUT)
GPIO.setup(LED_PIN[2], GPIO.OUT)


for i in LED_PIN:
    if(GPIO.input(BUTTON_PIN == GPIO.HIGH)):
       blink(i)


GPIO.cleanup()
