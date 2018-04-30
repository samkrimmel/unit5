#Sam Krimmel
#4/30/18
#antsDemo.py - using lists with graphics

from ggame import *
from random import randint


ANTS = 50
WIDTH = 900
HEIGHT = 600

#move each ant randomly up/down and left/right
def step():
    for ant in data['antList']:
        ant.x += randint(-10,10)
        ant.y += randint(-10,10)

#putting fire ants randomly on the screen
if __name__ == '__main__':
    
    data = {}
    data['antList'] = []
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(5,LineStyle(1,red),red)
    
    for i in range(ANTS):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)
