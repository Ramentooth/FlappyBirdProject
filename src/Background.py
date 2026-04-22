import pygame
from Settings import speed, screenL, screenH

class Background:
    def __init__(self,x,y,photo):
        self.x = x
        self.y = y
        self.x2 = x + screenL
        self.photo = photo
        self.photoSpeed = speed
        self.bg = pygame.image.load(self.photo).convert()
        self.Sbg = pygame.transform.scale(self.bg, (screenL, screenH))
        self.Sbg2 = pygame.transform.scale(self.bg, (screenL, screenH))
    def moveBG(self):
        self.x -= speed/1.5
        self.x2 -= speed/1.5
        if self.x <= -screenL:
            self.x = screenL
        if self.x2 <= -screenL:
            self.x2 = screenL
    def startScreen():
        pass
    def endScreen():
        pass


        
    
