#Sam Krimmel
#4/30/18
#antsDemo.py - using lists with graphics

from ggame import *
from random import randint


ANTS = 10
WIDTH = 800
HEIGHT = 800


if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(5,LineStyle(1,red),red)
    
    for i in range(ANTS):
        Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))
    
    Sprite(ant)
    
    App().run()
