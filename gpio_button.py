from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

## HARDWARE ##
led = LED(14)

## Gui Definitions ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

## Event Functions ##
def ledToggle():
	if led.is_lit:
		
	
## Widgets ##
ledButton = Button(win, text = "Turn LED On", font = myFont, command = ledToggle, bg = "bisque2", height = 1, width = 24)


