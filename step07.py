import pygame
import random
"""
STEP 07.바닥으로 떨어진 블록 고정 + 새 블록 등장
"""
pygame.init()

WIDTH, HEIGHT = 600, 900
BLOCK_SIZE = 40 # Tetris block cell
ROWS, COLS = HEIGHT // BLOCK_SIZE, WIDTH // BLOCK_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("step07-블록고정 새 블록 등장")

# color of tetris block 
COLORS = [(0,255,255), (0,0,255), (255,165,0),
          (255,255,0), (0,255,0), (128,0,128), (255,0,0)
          ]

# shape of Tetris block
BLOCKS = [
    [[1,1,1,1]], # I shape
    [[1,1],
     [1,1]], # O square  
    [[1,1,1], 
     [0,1,0]] # T shape
]

block = random.choice(BLOCKS)
color = random.choice(COLORS)
x, y = 5, 0 # 처음 블록 위치

# 시간 추적용 변수
drop_time = pygame.time.get_ticks()

# 블록 회전 함수 추가
def rotate(shape):
    rows = len(shape)
    cols = len(shape[0])
    rotated = []
    for j in range(cols):
        new_row = []
        for i in range(rows - 1, -1, -1): # 예. rows = 3, range(2, -1, -1) -> 2,1,0
            new_row.append(shape[i][j])
        rotated.append(new_row)
    return rotated


def rotate_zip(shape):
    return [list(row) for row in zip(*shape[::-1])]

# 충돌 감지 함수
def check_collision(shape, x, y):
    # 블록이 1인 것들
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]: # 블록이 1인 것들
                new_x = x + j # 현재 x 위치에서 블록만큼(j값) 더함 -> 현재위치에서 블록만큼 이동
                new_y = y + i
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return True
                if new_y >= 0 and board[new_y][new_x]: # new_y, new_x 자리에 이미 값(1)이 있으면 기존에 블록이 있다는 뜻 -> 기존 블록과 충돌이 일어남.
                    return True
    return False

# 블록을 보드에 고정 = 해당 부분에 color 칠하기
def place_block(shape, color, x, y):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                board[y+i][x+j] = color

# 보드 초기화
board = [[None for _ in range(COLS)] for _ in range(ROWS)]
"""
# 1. 
예. COLS = 10, ROWS = 25
[None for _ in range(COLS)] 
[None, None, None, None, None,None, None, None, None, None,]

# 2. for _ in range(ROWS)
[None, None, None, None, None,None, None, None, None, None,]
[None, None, None, None, None,None, None, None, None, None,]
[None, None, None, None, None,None, None, None, None, None,]
... 22줄

"""

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0,0,0)) # 화면 검은색으로 덮고 다시 화면 보여주기 위해서
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 방향키로 블록 이동
        elif event.type == pygame.KEYDOWN: # 키가 눌리는 이벤트 발생
            if event.key == pygame.K_LEFT and not check_collision(block, x - 1, y): # 눌린 키가 왼쪽 화살표키이면
                x -= 1 # 왼쪽 이동
            elif event.key == pygame.K_RIGHT and not check_collision(block, x + 1, y):
                x += 1 # 오른쪽 이동
            elif event.key == pygame.K_DOWN and not check_collision(block, x, y + 1):
                y += 1
            elif event.key == pygame.K_UP: # 회전
                new_block = rotate(block)
                if not check_collision(new_block, x, y):
                    block = new_block
                
    # 0.5초마다 블록이 한 칸씩 내려옴
    if pygame.time.get_ticks() - drop_time > 500:
        if not check_collision(block, x, y+1):
            y += 1
        else:
            place_block(block, color,x,y)
            block = random.choice(BLOCKS)
            color = random.choice(COLORS)
            x = COLS // 2 - len(block[0]) // 2
            y = 0    
            
        drop_time = pygame.time.get_ticks()
    
    # 보드 그리기
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col]:
                pygame.draw.rect(screen, board[row][col],
                    (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, (255, 255, 255),
                    (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    
    # 블록 그리기
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j]: 
                screen_x  = (x+j) * BLOCK_SIZE
                screen_y = (y+i) * BLOCK_SIZE
                
                pygame.draw.rect(screen, color, (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, (100,100,100), (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE),1)

    pygame.display.flip()
    # 초당 최대 30프레임 (30FPS) 제한
    clock.tick(30) # 1초에 최대 30번만 루프가 실행되게 만듦.

pygame.quit()