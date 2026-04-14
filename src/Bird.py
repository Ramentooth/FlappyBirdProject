import pygame

class Bird:
    def __init__(self,x,y,w,h,type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
        self.velocity = 0
        self.GRAVITY = 0.02
        self.BOOST = -25

    def drawBird(self):
        bird = (self.x - 50, self.y - 50, self.w, self.h)
        return bird

    def gravity(self,SPACECLICKED):
        if SPACECLICKED:
            self.y += self.BOOST
            self.velocity = 0
        self.y += self.velocity
        self.velocity += self.GRAVITY
        
    def birdType(self):
        pass

    def controls(self):
        pass
