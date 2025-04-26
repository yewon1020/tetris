import pygame
import random
"""
STEP 03.테트리스 블록을 한 개만 그리기
"""
pygame.init()

WIDTH, HEIGHT = 600, 900
BLOCK_SIZE = 40 # Tetris block cell
ROWS, COLS = HEIGHT // BLOCK_SIZE, WIDTH // BLOCK_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("step03 - 테트리스 블록 하나 그리기")

# color of tetris block
COLORS = [(0,255,255), (0,0,255), (225,165,0),
          (255,255,0), (0,255,0), (128,0,128), (255,0,0)
          ]

# shape of tetris block
BLOCKS = [[[1,1,1,1]], # I
          [[1,1],[1,1]], # square
          [[1,1,1], [0,1,0]], # T shape        
]

block = random.choice(BLOCKS)
color = random.choice(COLORS)
x, y = 5, 5 # 5칸 X 5칸 위치에 그리기



running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    screen.fill((0,0,0)) # black

    print(block)
    for i in range(len(block)) :
        for j in range(len(block[i])) :
            if block[i][j] :
                screen_x = (x+j) * BLOCK_SIZE
                screen_y = (y+i) * BLOCK_SIZE

                #print(f"block coord({x+j}, {y+i}) -> screen coord ({screen_x}, {screen_y})")

                # draw block
                pygame.draw.rect(screen, color, (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
                # 회색 테두리
                pygame.draw.rect(screen,(100,100,100), (screen_x, screen_y,BLOCK_SIZE,BLOCK_SIZE),1)


    pygame.display.flip()       


pygame.quit()