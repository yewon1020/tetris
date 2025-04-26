import pygame
import random
"""
STEP 04. 블록 자동으로 내려오기기
"""
pygame.init()

WIDTH, HEIGHT = 600, 900
BLOCK_SIZE = 40 # Tetris block cell
ROWS, COLS = HEIGHT // BLOCK_SIZE, WIDTH // BLOCK_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("step04 - 블록 자동으로 내려오기기")

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
x, y = 5, 0 # 처음 블록 위치

# 시간 추적용 변수 : 게임 시작 후 흐른 시간
drop_time = pygame.time.get_ticks() # drop time에 지금 시간을 체크한 것을 넣음음



running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    screen.fill((0,0,0)) # black

    # 현재 시각 - 이전에 측정한 시각이 500ms 보다 커지면
    # 0.5 ->
    if pygame.time.get_ticks() - drop_time > 500 : # 또 지금 시간을 기록함
        y += 1 # 500보다 크면 아래로 한 칸 이동
        drop_time = pygame.time.get_ticks
        drop_time = pygame.time.get_ticks() # 또 시간 기록



    # 블록 그리기
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