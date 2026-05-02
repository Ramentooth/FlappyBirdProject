import pygame
pygame.mixer.init()

class Bird:
    def __init__(self,x,y,w,h,type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
        self.velocity = 0
        self.GRAVITY = 0.02
        self.BOOST = 0
        self.flappySFX = pygame.mixer.Sound('FlappyJump.mp3')
        self.birdPicUp = pygame.transform.scale(pygame.image.load('birdPicDown.jpg').convert_alpha(), (50, 50))
        self.birdGlide = pygame.transform.scale(pygame.image.load('birdGlide.jpg').convert_alpha(), (50, 50))
        #self.unscaledPicDown = Background(self.x, self.y, 'birdPicDown')
        #self.birdPicDown = Background(self.x, self.y, 'birdPicDown')

    def birdPos(self):
        bird = (self.x - 50, self.y - 50, self.w, self.h)
        return bird

    def gravity(self,SPACECLICKED):
        if SPACECLICKED:
            self.flappySFX.play()
            self.BOOST = -2.3
            self.velocity = 0

        self.y += self.velocity
        self.velocity += self.GRAVITY
        self.y += self.BOOST
        self.BOOST += self.GRAVITY
        
    def birdType(self):
        pass

    def birdImage(self):
        if self.velocity < 0:
            return self.birdPicUp   
        else:
            return self.birdGlide
