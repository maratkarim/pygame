# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:09:23 2020

@author: MARAT
"""

import pygame
import random

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))

score_sur = pygame.Surface((100,20))

score_shrift = pygame.font.Font(None, 30)

done = False

backgroundImage = pygame.image.load('background.jpg')

playerImage = pygame.image.load('player.png')

player_x = 200
player_y = 500

bulletImage=pygame.image.load('bullet.png')

enemyImage = pygame.image.load('enemy.png')

enemy_x = random.randint(0, 536)
enemy_y = random.randint(20, 50)

enemy_dx = 10
enemy_dy = 10

bullet_x=player_x
bullet_y=player_y

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def bullet(x,y):
    screen.blit(bulletImage,(x,y))

score=0




while not done:
    for event in pygame.event.get():
        # event on quit
        if event.type == pygame.QUIT: # event.type == pygame.KEYDOWN
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: 
        player_x -= 15
        bullet_x=player_x
    if pressed[pygame.K_RIGHT]:
        player_x += 15
        bullet_x=player_x
    screen.fill((0, 0, 0))  
    bullet_y-=60
    if bullet_y<0 or bullet_y==enemy_y:
        bullet_y=player_y
        if bullet_y<player_y:
            bullet_x=player_x
    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x > 536:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy
    for i in range(enemy_x+8,enemy_x+32):
        if bullet_x==i:
            enemy_x = random.randint(0, 536)
            enemy_y = random.randint(20, 50)
            score+=1

    score_sur.fill((0,0,0))
    score_sur.blit(score_shrift.render("SCORE:"+str(score), 1, (255,255,255)), (0,0))
    
    screen.blit(backgroundImage, (0, 0))
    player(player_x, player_y)
    bullet(player_x,player_y)
    enemy(enemy_x, enemy_y)
    screen.blit(score_sur,(0,0))
    bullet(bullet_x,bullet_y)
    pygame.display.flip()
    clock.tick(15)