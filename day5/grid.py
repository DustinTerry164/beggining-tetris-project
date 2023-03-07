import pygame.image
import updating_grid,pieces
global score, falling_speed, moving_right, moving_left, current_piece,passive_grid
score = 0
red_cube = pygame.image.load("red_cube.png")
blue_cube = pygame.image.load("blue_cube.png")
green_cube = pygame.image.load("green_cube.png")
cubes = [red_cube,blue_cube,green_cube]

#passive grid is 14 blocks tall
passive_grid = [[0,0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]]

def test_block_collision():

    if(int(updating_grid.piece_pos_y) == 18 - len(pieces.current_piece)): #check if the piece has hit the bottom of the screen
        place_piece()

    for y in range(len(passive_grid)):
        for x in range(len(passive_grid[y])): #check if a piece is above a placed piece
            if passive_grid[y][x] >= 1 and updating_grid.active_grid[y+3][x] >= 1:
                place_piece()

def place_piece():
    updating_grid.falling_speed = 0
    for y in range(len(updating_grid.active_grid)):
        for x in range(len(updating_grid.active_grid[y])):
            if(y - 4>= 0): #prevent out of bounds exception
                if(passive_grid[y-4][x] == 0):
                    passive_grid[y-4][x] = updating_grid.active_grid[y][x] #copies the entire active grid to the passive grid

    updating_grid.piece_pos_y = 0
    updating_grid.piece_pos_x = 4
    updating_grid.falling_speed = updating_grid.target_speed
    pieces.randomized_piece()


def  update_and_compare_grids(piece):
    updating_grid.clear_active_grid()
    for y in range(len(updating_grid.active_grid)):
            for piece_height in range(len(piece)):#cycle through the selected piece
                for piece_width in range(len(piece[piece_height])):#cycle through the width of the piece

                    if  int(updating_grid.piece_pos_x) + piece_width < 10 and  not int(updating_grid.piece_pos_x) + piece_width < 0: #only add the block to the grid if its fully on the grid
                       try:
                           updating_grid.active_grid[int(updating_grid.piece_pos_y) + piece_height][int(updating_grid.piece_pos_x) + piece_width] = piece[piece_height][piece_width]  # add piece to the active grid
                       except IndexError:
                           return 0

                    updating_grid.test_sidewall_collision(piece_width)


def shift_rows(row):
      current_row = row
      while current_row != 0:
                for x in range(len(passive_grid[current_row])) :
                       passive_grid[current_row][x]=passive_grid[current_row-1][x]
                current_row -=1

def check_changes():
       global  score, current_piece

       update_and_compare_grids(pieces.get_current_piece())

       test_block_collision()
       updating_grid.check_movement()
       for y in range(len(passive_grid)): #loop through the passive grid and check if each line is full then clear and shift it if it is
           count = 0
           for x in range(len(passive_grid[y])):
                 if passive_grid[y][x] != 0:
                     count += 1
                     if(count >= 10):
                       score += 100
                       shift_rows(y)
