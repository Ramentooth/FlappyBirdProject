import pygame
from Settings import screenH, screenL, speed

class Buttons:
    def __init__(self,x,y,w,h,cMain,cDown): #cText,cShade
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cMain = cMain
        self.cDown = cDown
        self.clickedVal = False
        self.display = True
        #self.cText = cText
        #self.cSshade = cShade

    def drawButton(self, screen, mousX, mousY, MOUSEBUTTONUP, MOUSEBUTTONDOWN, otherStartVal):
        if self.display:
            if (self.x - self.w/2) <= mousX <= ((self.x - self.w/2) + self.w) and (self.y - self.h/2) <= mousY <= ((self.y - self.h/2) + self.h):
                pygame.draw.rect(screen, self.cDown, ((self.x - self.w/2), (self.y - self.h/2), self.w, self.h), 0, 20)
                if MOUSEBUTTONDOWN and MOUSEBUTTONUP != True:
                    self.clickedVal = True
                    self.display = False
            elif otherStartVal:
                self.clickedVal = True
                self.display = False
            else:
                pygame.draw.rect(screen, self.cMain, ((self.x - self.w/2), (self.y - self.h/2), self.w, self.h), 0, 20)
            
    def gravity():
        pass
        

        


        
