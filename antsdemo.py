#Astro Ohnuma
#11/20/17
#antsdemo.py - how to use lists with graphics

from ggame import *
from random import randint

WIDTH = 800
HEIGHT = 400

def step():
    for ant in data['antlist']:
        ant.x += 1
        ant.y += 1

if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    data = {}
    data['antlist'] = []
    
    for i in range(10):
        data['antlist'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)
