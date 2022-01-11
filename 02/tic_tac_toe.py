#***********************************************************************
# Homework:
#    tic_tac_toe.py
#    Brother Lythgoe, CSE210
# Author:
#    Mario Flota
# Summary:  Tic-Tac-Toe Game.
#**********************************************************************

def main():
    grid = create_grid()
    play = 1
    while not (draw(grid) or is_a_win(grid)):
        draw(grid)
        make_a_move(play, grid)
        play += 1
    draw(grid)
    print('Great game! Thanks for playing!')

def create_grid():
    grid = []
    for i in range(9):
        grid.append(i + 1)
    return grid

def draw(grid):
    print()
    print(f'{grid[0]} | {grid[1]} | {grid[2]}')
    print('--+---+--')
    print(f'{grid[3]} | {grid[4]} | {grid[5]}')
    print('--+---+--')
    print(f'{grid[6]} | {grid[7]} | {grid[8]}')
    print()

def make_a_move(play, grid):
    if play % 2 == 0:
        turn = int(input("X's turn, choose a square from 1-9: "))
        player = "X"
    else:
        turn = int(input("O's turn, choose a square from 1-9: "))
        player = "O"
    grid[turn - 1] = player 

def is_a_win(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])

def check_draw(grid):
    for i in range(9):
        if grid[i] != 'X' and grid[i] != 'O':
            return False
    return True

if __name__ == "__main__":
    main()