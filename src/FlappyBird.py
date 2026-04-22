# IMPORTS

import pygame
from Background import Background
from Bird import Bird
from Button import Buttons
from Pipe import Pipe
from Settings import screenH, screenL, speed, screen, pipeC, font

# CLASS INSTANTIATIONS
pipes = [
Pipe(1200, 0, "pipe"),
Pipe(1700, 0 , "pipe"),
Pipe(2200, 0 , "pipe")
]
bird1 = Bird(500, 500, 50, 50, "none")
startB = Buttons((screenL/2), (screenH/2), 100, 100, 255, 255, 'START')
field = Background(0,0,'fieldBG.jpeg')
gameOverScreen = Background(0,0,'FlappyGameOver.jpeg')
replayB = Buttons((screenL/2), (screenH/2), 100, 100, 255, 255, 'PLAY AGAIN')

clock = pygame.time.Clock()

MOUSEBUTTONUP = False
MOUSEBUTTONDOWN = False
SPACECLICKED = False
score = 0
canScore = False
gameOver = False

pygame.display.set_caption('FLAPPY BIRD by Simon Sakata 3B 2026')

# MAIN GAME LOOP

running = True
while running:

    #print(pygame.key.())
    

    mousX, mousY = pygame.mouse.get_pos()
    screen.fill((255,255,255))
    screen.blit(field.Sbg, (field.x,field.y))
    screen.blit(field.Sbg2, (field.x2,field.y))

    Buttons.drawButton(startB, screen, mousX, mousY, MOUSEBUTTONUP, MOUSEBUTTONDOWN, SPACECLICKED)

    SPACECLICKED = False

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            MOUSEBUTTONUP = True
            MOUSEBUTTONDOWN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSEBUTTONDOWN = True
            MOUSEBUTTONUP = False
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                SPACECLICKED = True
    if startB.clickedVal: #initiates running game after start button is pressed
        field.moveBG()

        text = font.render(f"Score: {score}", True, (0))
        screen.blit(text,(100,100))

        for pipe in pipes:
            Pipe.movePipes(pipe)
            for top, bottom, topRim, bottomRim, scoreRect, resetRect in Pipe.makePipes(pipe):
                pygame.draw.rect(screen, pipeC, top) # draws visible TOP pipe
                pygame.draw.rect(screen, pipeC, topRim) # draws visible RIM on TOP pipe
                pygame.draw.rect(screen, pipeC, bottom) # draws visible BOTTOM pipe
                pygame.draw.rect(screen, pipeC, bottomRim) # draws visible RIM on BOTTOM pipe


                topPipeRect = pygame.Rect(top) # draws collision rectangle for top pipe
                bottomPipeRect = pygame.Rect(bottom) # draws collision rectangle for bottom pipe

                Bird.gravity(bird1,SPACECLICKED)
                pygame.draw.rect(screen, (255,0,0), Bird.drawBird(bird1)) # draws visible bird
                birdRect = pygame.Rect(Bird.drawBird(bird1)) # draws collsion rectangle for bird
                floor = pygame.Rect(0,screenH,screenL,1)
                roof = pygame.Rect(0,-100,screenL,100)

                resetRec = pygame.Rect(resetRect)
                if birdRect.colliderect(resetRec):
                    canScore = True
                elif canScore:
                    scoreRec = pygame.Rect(scoreRect)
                    if birdRect.colliderect(scoreRec):
                        score += 1
                        canScore = False

                if birdRect.colliderect(topPipeRect) or birdRect.colliderect(bottomPipeRect) or birdRect.colliderect(floor) or birdRect.colliderect(roof):
                    startB.clickedVal = False
                    running = True
                    gameOver = True
                    
    if gameOver:
        screen.blit(gameOverScreen.Sbg,(gameOverScreen.x, gameOverScreen.y))
        Buttons.drawButton(replayB, screen, mousX, mousY, MOUSEBUTTONUP, MOUSEBUTTONDOWN, SPACECLICKED)
        if replayB.clickedVal:
            gameOver = False
            startB.clickedVal = True

    pygame.display.flip()
    clock.tick(60)
