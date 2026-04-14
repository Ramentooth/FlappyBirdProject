import pygame
from Settings import screenH, speed

class Backgrounds:
    def __init__(self,screenMoving,photo):
        self.screenMoving = screenMoving
        self.photo = photo
    def displayBackgound(self):
