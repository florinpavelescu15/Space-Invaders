import pygame
import math
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 200
playerY = 560
playerX_change = 0

ex = []
ey = []
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 55
for i in range(number_of_enemies):
    if i >= 0 and i < 11:
        enemyImg.append(pygame.image.load('invader1.png'))
        enemyX.append(50+(i % 11)*50)
        enemyY.append(40+(i/11)*50)
        ex.append(50+(i % 11)*50)
        ey.append(40+(i/11)*50)
    if i >= 11 and i < 22:
        enemyImg.append(pygame.image.load('invader2.png'))
        enemyX.append(50+(i % 11)*50)
        enemyY.append(40+(i/11)*50)
        ex.append(50+(i % 11)*50)
        ey.append(40+(i/11)*50)
    if i >= 22 and i < 33:
        enemyImg.append(pygame.image.load('invader3.png'))
        enemyX.append(50+(i % 11)*50)
        enemyY.append(40+(i/11)*50)
        ex.append(50+(i % 11)*50)
        ey.append(40+(i/11)*50)
    if i >= 33 and i < 44:
        enemyImg.append(pygame.image.load('invader4.png'))
        enemyX.append(50+(i % 11)*50)
        enemyY.append(40+(i/11)*50)
        ex.append(50+(i % 11)*50)
        ey.append(40+(i/11)*50)
    if i >= 44 and i < 55:
        enemyImg.append(pygame.image.load('invader5.png'))
        enemyX.append(50+(i % 11)*50)
        enemyY.append(40+(i/11)*50)
        ex.append(50+(i % 11)*50)
        ey.append(40+(i/11)*50)
    enemyX_change.append(1)
    enemyY_change.append(20)

bx = []
by = []
bunkerImg = []
bunkerX = []
bunkerY = []
number_of_bunkers = 6
for i in range(number_of_bunkers):
    bunkerImg.append(pygame.image.load('bunker.png'))
    bunkerX.append(50+(i % 6)*125)
    bunkerY.append(500)
    bx.append(50+(i % 6)*125)
    by.append(500)

bulletImg = pygame.image.load('bullet1.png')
bulletX = 200
bulletY = 560
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

bullet2Img = pygame.image.load('bullet2.png')
bullet2X = 200
bullet2Y = 560
bullet2X_change = 0
bullet2Y_change = 1
bullet2_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

high_score_value = 0
htextY = 10
htextX = 500


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))


def fire_bullet2(x, y):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2Img, (x, y))


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    if distance < 30:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score:"+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_high_score(x, y):
    high_score = font.render(
        "High score:"+str(high_score_value), True,  (255, 255, 255))
    screen.blit(high_score, (x, y))


def show_game_over(x, y):
    game_over = font.render("GAME OVER", True, (255, 255, 255))
    left_exit = font.render(
        "PRESS THE LEFT ARROW KEY TO EXIT", True, (255, 255, 255))
    right_continue = font.render(
        "PRESS THE RIGHT ARROW KEY TO CONTINUE", True, (255, 255, 255))
    screen.fill((0, 0, 51))
    screen.blit(game_over, (x, y))
    screen.blit(left_exit, (x, y+200))
    screen.blit(right_continue, (x, y+100))
    pygame.display.update()


running = True

while True:
    while running:
        screen.fill((0, 0, 51))

        for i in range(number_of_bunkers):
            screen.blit(bunkerImg[i], (bunkerX[i], bunkerY[i]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -2
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX = playerX+playerX_change

        if playerX < 0:
            playerX = 0
        if playerX > 768:
            playerX = 768

        for i in range(number_of_enemies):
            enemyX[i] = enemyX[i]+enemyX_change[i]

            for k in range(11):
                for j in range(55):
                    if j % 11 == k and enemyX[j] >= 0:
                        left = j
                        break
                break

            for l in range(10, -1, -1):
                for j in range(55):
                    if j % 11 == l and enemyX[j] <= 800 and enemyX[j] >= 0:
                        right = j
                        break
                break

            if enemyX[left] <= 0:
                enemyX_change[i] = 1
                enemyY[i] = enemyY[i]+enemyY_change[i]
            if enemyX[right] >= 768:
                enemyX_change[i] = -1
                enemyY[i] = enemyY[i]+enemyY_change[i]

            collision1 = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision1:
                bulletY = 560
                bullet_state = "ready"
                enemyX[i] = -100000
                enemyY[i] = -100000
                score_value = score_value+1

            enemy(enemyX[i], enemyY[i], i)

            if bullet2_state is "ready":
                bullet2Y = enemyY[i]
                bullet2X = random.uniform(enemyX[left], enemyX[right])
                fire_bullet2(bullet2X, bullet2Y)

            if bullet2Y >= 600:
                bullet2Y = enemyY[i]
                bullet2_state = "ready"
            if enemyY[i] > 550:
                running = False

        for i in range(number_of_bunkers):
            collision2 = isCollision(bunkerX[i], bunkerY[i], bulletX, bulletY)
            if collision2:
                bulletY = 568
                bullet_state = "ready"
                bunkerX[i] = -100000
                bunkerY[i] = 100000

        for i in range(number_of_bunkers):
            collision3 = isCollision(
                bunkerX[i], bunkerY[i], bullet2X, bullet2Y)
            if collision3:
                bullet2_state = "ready"
                bunkerX[i] = -100000
                bunkerY[i] = 100000

        collision4 = isCollision(playerX, playerY, bullet2X, bullet2Y)
        if collision4:
            running = False
            playerX = 100000
            playerY = 100000

        if bullet2_state is "fire":
            fire_bullet2(bullet2X, bullet2Y)
            bullet2Y = bullet2Y+bullet2Y_change

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY = bulletY-bulletY_change
        if bulletY <= 0:
            bulletY = 568
            bullet_state = "ready"

        player(playerX, playerY)
        show_score(textX, textY)
        show_high_score(htextX, htextY)
        pygame.display.update()

    show_game_over(10, 100)

    if high_score_value < score_value:
        high_score_value = score_value

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX = 200
                playerY = 560
                playerX_change = 0

                for i in range(number_of_enemies):
                    enemyX[i] = ex[i]
                    enemyY[i] = ey[i]
                    enemyX_change.append(1)
                    enemyY_change.append(15)

                for i in range(number_of_bunkers):
                    bunkerX[i] = bx[i]
                    bunkerY[i] = by[i]

                bulletX = 200
                bulletY = 560
                bulletX_change = 0
                bulletY_change = 4
                bullet_state = "ready"
                bullet2X = 200
                bullet2Y = 560
                bullet2X_change = 0
                bullet2Y_change = 1
                bullet2_state = "ready"
                score_value = 0
                running = True
            else:
                if event.key == pygame.K_LEFT:
                    exit()
            break
