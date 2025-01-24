import sys, pygame
import random
import os
import math
import random
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
direction = 0 
speed = 1
ball_pos = [225,225]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill("gray")
    
    if ball.colliderect(paddle1):
        direction += 180
        height = ball.centery - paddle1.centery
        direction += height / 2
    
    if ball.colliderect(paddle2):
        direction += 180
        height = ball.centery - paddle2.centery
        direction -= height / 2
        
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        paddle2.y+=5
    
    if pygame.key.get_pressed()[pygame.K_UP]:
        paddle2.y-=5
    
    if pygame.key.get_pressed()[pygame.K_w]:
        paddle1.y-=5
        
    if pygame.key.get_pressed()[pygame.K_s]:
        paddle1.y+=5
        
    #move the ball
    x = math.cos(math.radians(direction)) * speed 
    y = math.sin(math.radians(direction)) * speed
    
    ball_pos[0] += x
    ball_pos[1] += y
    
    ball.center = ball_pos
    
    pygame.draw.rect(screen, "white", paddle1)
    pygame.draw.rect(screen, "white", paddle2)
    pygame.draw.circle(screen, "green", ball.center, 5)
    pygame.display.update()
    clock.tick(100)