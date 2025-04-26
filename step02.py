import pygame
"""
STEP 02. 윈도우에 grid 만들기
블록 위치 조정을 위한 grid
"""
pygame.init()

WIDTH, HEIGHT = 600, 900
BLOCK_SIZE = 40 # Tetris block cell
ROWS, COLS = HEIGHT // BLOCK_SIZE, WIDTH // BLOCK_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("step02 - grid 만들기")

running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    screen.fill((0,0,0)) # black

    # grid
    # range(start,end,step) -> range(0,10,2) -> 0,2,4,6,......
    # x = BLOCK_SIZE * 0 , BLOCK_SIZE * 1, BLOCK_SIZE * 2,.........
    for x in range(0, WIDTH, BLOCK_SIZE) :
        pygame.draw.line(screen, (225,225,225), (x,0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE) :
        pygame.draw.line(screen, (225,225,225), (0,y), (WIDTH,y))

    pygame.display.flip()       


pygame.quit()