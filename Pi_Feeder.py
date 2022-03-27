from gpiozero import Servo
import time
from time import sleep

myGPIO = 17

start = time.time()

Duration = 3

myServo = Servo(myGPIO)

while True:
	myServo.min()
	sleep(1)
	if time.time() > start + Duration:
		break
	exit()	