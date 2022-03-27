# SPDX-FileCopyrightText: 2021 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT
# RaspberryPi Pico RP2040 Mechanical Keyboard
 
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
 
print("---Pico Pad Keyboard---")
 
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True
 
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
 
# list of pins to use (skipping GP15 on Pico because it's funky)
pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
]
 
MEDIA = 1
KEY = 2
 
keymap = {
    (0): (KEY, [Keycode.ONE]),
    (1): (KEY, [Keycode.UP_ARROW]),
    (2): (KEY, [Keycode.THREE]),
    (3): (KEY, [Keycode.LEFT_ARROW]),
    (4): (KEY, [Keycode.FIVE]),
    (5): (KEY, [Keycode.RIGHT_ARROW]),
    (6): (KEY, [Keycode.SEVEN]),
    (7): (KEY, [Keycode.DOWN_ARROW]),
    (8): (KEY, [Keycode.NINE]),

}
switches = [0, 1, 2, 3, 4, 5, 6,
            7, 8]
 
for i in range(9):
    switches[i] = DigitalInOut(pins[i])
    switches[i].direction = Direction.INPUT
    switches[i].pull = Pull.UP
 
switch_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
 
while True:
    for button in range(9):
        if switch_state[button] == 0:
            if not switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.press(*keymap[button][1])
                    else:
                        cc.send(keymap[button][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state[button] = 1
 
        if switch_state[button] == 1:
            if switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])
 
                except ValueError:
                    pass
                switch_state[button] = 0
 
    time.sleep(0.01)  # debounce
