# Snake Game in Python

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set screen size
screenSize = screenWidth, screenHeight = 840, 680
screen = pygame.display.set_mode(screenSize)

# Set window caption
pygame.display.set_caption('MySnake')

# Colors
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

red = pygame.Color(255, 0, 0)

# FPS controller
fpsController = pygame.time.Clock()

# Initialize game variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, screenWidth // 10) * 10, random.randrange(2, screenHeight // 10) * 10]
foodSpawn = True

direction = 'RIGHT'
changeDirection = direction

score = 0

# Game Over
def gameOver():
    # Game over font
    gameOverFont = pygame.font.SysFont('monaco', 72)
    gameOverSurf = gameOverFont.render('Game Over!', True, red)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (screenWidth // 2, screenHeight // 4)
    screen.blit(gameOverSurf, gameOverRect)
    showScore(0)
    pygame.display.flip()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Score
def showScore(choice=1):
    scoreFont = pygame.font.SysFont('monaco', 24)
    scoreSurf = scoreFont.render('Score : {0}'.format(score), True, white)
    scoreRect = scoreSurf.get_rect()
    if choice == 1:
        scoreRect.midtop = (screenWidth // 2, 10)
    else:
        scoreRect.midtop = (screenWidth // 2, screenHeight // 2)
    screen.blit(scoreSurf, scoreRect)

# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Keystrokes are detected
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeDirection = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeDirection = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeDirection = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeDirection = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of direction
    if changeDirection == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeDirection == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeDirection == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeDirection == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Moving snake in direction
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # Snake body
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    # Spawn food on screen
    if foodSpawn == False:
        foodPos = [random.randrange(1, screenWidth // 10) * 10, random.randrange(1, screenHeight // 10) * 10]
    foodSpawn = True

    # Background
    screen.fill(black)

    # Draw snake
    for pos in snakeBody:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, red, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    # Bound
    if snakePos[0] < 0 or snakePos[0] > screenWidth - 10:
        gameOver()
    if snakePos[1] < 0 or snakePos[1] > screenHeight - 10:
        gameOver()

    # Self hit
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(24)