import pygame
import random
from Settings import screenH, screenL, speed, gap, pipeW, rimW, rimL 

class Pipe:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        self.spaceGen = random.randint(50,450)
    def movePipes(self):
        self.x -= speed
        if self.x == -pipeW:
            self.x += screenL + 100
            self.spaceGen = random.randint(50,450)



    def displayPipes(self):
        pass
    def makePipes(self):
        topL = self.spaceGen
        bottomY = topL + gap 
        bottomL = screenH - bottomY 
        top = (self.x, 0, pipeW, topL)
        topRim = (self.x - rimW, topL - rimL, pipeW + rimW + rimW, rimL)
        bottom = (self.x, bottomY, pipeW, bottomL)
        bottomRim = (self.x - rimW, bottomY, pipeW + rimW + rimW, rimL)
        yield top, bottom, topRim, bottomRim
