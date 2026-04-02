import pygame
#from Background import Backgrounds
#from Bird import Birds
#from Button import Buttons
#from Pipe import Pipes

screen = pygame.display.set_mode((700,700))

running = True
while running:
    screen.fill(0)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False