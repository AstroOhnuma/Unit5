#Astro Ohnuma
#11/16/17
#bettercoloredwindow.py - coloredwindow.py except using a list instead of if statements

from ggame import *
from random import randint

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
blackoutline = LineStyle(1,black)
    
redbackground = RectangleAsset(600,600,blackoutline,red)
greenbackground = RectangleAsset(600,600,blackoutline,green)
bluebackground = RectangleAsset(600,600,blackoutline,blue)

colors = [redbackground, greenbackground, bluebackground]

def mouseclick(event):
    num = randint(0,2)
    Sprite(colors[num])
App().listenMouseEvent('click', mouseclick)
App().run()
