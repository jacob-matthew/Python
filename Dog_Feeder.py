from machine import Pin,PWM
import time
import blynklib

BLYNK_AUTH = '<YourAuthToken>' #insert your Auth Token here

blynk=blynklib.Blynk(BLYNK_AUTH)
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
servo = PWM(Pin(2),freq = 50, duty = 255)

while True:
    if button.value = 1:
        servo.duty(30)
        time.sleep(1)
    servo.duty(160)
    time.sleep(1)
            