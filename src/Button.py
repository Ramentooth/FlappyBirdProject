import pygame
from Settings import screenH, screenL, speed, font

class Buttons:
    def __init__(self,x,y,w,h,cMain,cDown,text,cText,cButton,cButtonDown): #cText,cShade
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cMain = cMain
        self.cDown = cDown
        self.text = text
        self.clickedVal = False
        self.display = True
        self.cText = cText
        self.cButton = cButton
        self.cButtonDown = cButtonDown
        #self.cSshade = cShade

    def drawButton(self, screen, mousX, mousY, MOUSEBUTTONUP, MOUSEBUTTONDOWN, SPACECLICKED):
        if self.display:
            if (self.x - self.w/2) <= mousX <= ((self.x - self.w/2) + self.w) and (self.y - self.h/2) <= mousY <= ((self.y - self.h/2) + self.h):
                pygame.draw.rect(screen, self.cDown, ((self.x - self.w/2), (self.y - self.h/2), self.w, self.h), self.cDown, 20)
                Bfont = pygame.font.SysFont(None,32)
                Btext = Bfont.render(self.text, True, (0,0,0), (255,255,255))
                textRect = Btext.get_rect(center=(self.x,self.y))
                screen.blit(Btext,textRect)
                if MOUSEBUTTONDOWN and MOUSEBUTTONUP != True or SPACECLICKED:
                    self.clickedVal = True
                    self.display = False
            elif SPACECLICKED:
                self.clickedVal = True
                self.display = False
            else:
                pygame.draw.rect(screen, self.cMain, ((self.x - self.w/2), (self.y - self.h/2), self.w, self.h), 0, 20)
                Bfont = pygame.font.SysFont(None,32)
                Btext = Bfont.render(self.text, True, (0,0,0), (255,255,255))
                textRect = Btext.get_rect(center=(self.x,self.y))
                screen.blit(Btext,textRect)
    def gravity():
        pass
        

        


        
