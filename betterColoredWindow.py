#Sam Krimmel
#4/25/18
#betterColoredWindow.py

from random import randint
from ggame import *

colors = [Color(0xFFFFFF,1),Color(0x000000,1),Color(0xFFE500,1),Color(0x4DA9F9,1),Color(0xFF0F0F,1),Color(0x08D63F,1)]

def mouseClick(event):
    color = colors[randint(1,7)-1]
    window = RectangleAsset(800,600,LineStyle(1,color),color)
    Sprite(window)

App().listenMouseEvent('click',mouseClick)
App().run()
