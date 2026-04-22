import pygame
pygame.font.init()

# SCREEN VARIABLES
screenH = 700
screenL = 1500
screen = pygame.display.set_mode((screenL, screenH))

# GAMEPLAY VARIABLES
speed = 6
gap = 150
pipeW = 100

# PIPE DESIGN
rimW = 10
rimL = 30
pipeC = (0, 255, 100)

# TEXT
font = pygame.font.SysFont(None, 64)

