import sys, pygame
import random
import os
import math
os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()
screen = pygame.display.set_mode([500,500])
clock= pygame.time.Clock()

def distance(p1,p2):
    A = p2[0] - p1[0]
    B = p2[1] - p1[1]
    
    return math.sqrt(A*A + B*B)



# creating objects
paddle1 = pygame.Rect(20,212,15,75)
paddle2 = pygame.Rect(465,212,15,75)
ball = pygame.Rect(245,250,10,10)

#creating varibles
hit = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill("gray")
    if hit % 2 == 0:
        ball.x += 1
    else:
        ball.x -= 1
    
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        hit += 1
        
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        paddle2.y+=5
    
    if pygame.key.get_pressed()[pygame.K_UP]:
        paddle2.y-=5
    
    if pygame.key.get_pressed()[pygame.K_w]:
        paddle1.y-=5
        
    if pygame.key.get_pressed()[pygame.K_s]:
        paddle1.y+=5
    
    pygame.draw.rect(screen, "white", paddle1)
    pygame.draw.rect(screen, "white", paddle2)
    pygame.draw.circle(screen, "green", ball.center, 5)
    pygame.display.update()
    clock.tick(100)