import utime
import machine

button = machine.Pin(4, machine.Pin.IN.PULL_DOWN)
servo = PWM(Pin(2), freq = 50, duty = 256)

while True:
    if button.value() == 1:
        print('Dispensing Food')
        servo.duty(100)
        utime.sleep(1)
    else:
        servo.duty(0)
        utime.sleep(1)
    servo.duty(0)        
        