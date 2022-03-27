import pyautogui

pyautogui.click(100, 100)
pyautogui.moveTo(100, 150)
pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
pyautogui.dragTo(100, 150)
pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

import mouse
# Number of pixels to move by on x and y axis
x = 1
y = 2
mouse.move(x, y)

import autopy # pip install autopy
autopy.mouse.smooth_move(100, 600)

import pyautogui as pg
clk= pg.locateOnScreen('click.png', confidence=0.9)
pg.click(x=clk.left+int(clk.width/2), y=clk.top+int(clk.height/2))
