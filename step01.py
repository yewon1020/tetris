import pygame
"""
pygame 기본 설정
STEP 01. 빈 창 띄우기
"""
pygame.init()

WIDTH, HEIGHT = 600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("step01 - 빈 창 띄우기")

running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    screen.fill((0,0,0)) # black
    pygame.display.flip()       

pygame.quit()