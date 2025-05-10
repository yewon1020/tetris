## Introduction
Tetris is game which you have to stack the block. You can get point and there's no end(but if you stack the block until the top, you are out!).
## How to play 
You have to stack the block and clear the lines. You can use the direction keys to move the block. 
When you press the up key, you can turn the block. Also, when you press the space key, you can move the block to the bottom at once. 
If you clear the lines, you can get point. In 1 line, you get 100 points. When you reach 500, the level will increase.
Good luck!
## Preview
![녹음 2025-05-10 172004 (2)](https://github.com/user-attachments/assets/045a304d-65b7-42a9-ab62-a6e9564cfc28)
## About some logic

```python
def clear_lines() :
    global board 
    new_board = []
    lines_removed = 0
    for row in board :
        if all (cell is not None for cell in row) : # if the cell is full
        else :     
            new_board.append(row) # get the values of rows and put them in new_board 
    while len(new_board) < ROWS :
        new_board.insert(0, [None for _ in range(COLS)]) # index add None to the 0th digit
    board = new_board
    return lines_removed  

```
```python
def check_collision(shape, x, y):
    # things with block cell values of 1
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]: # things with block cell values of 1
                new_x = x + j # add (j value) blocks from the current x position -> Move blocks from the current position
                new_y = y + i
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return True
                if new_y >= 0 and board[new_y][new_x]: # If there is already a value (1) in the new_y, new_x digits, it means that there is an existing block -> conflicts with the existing block.
                    return True
    return False

```
