import pygame.image
import updating_grid,pieces,random
global score, falling_speed, moving_right, moving_left, current_piece
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

def randomized_piece():
    random_value = random.randrange(0,8,1)
    if(random_value == 0): pieces.set_piece_target("Cube_piece")
    if (random_value == 1): pieces.set_piece_target("Long_piece")
    if (random_value == 2): pieces.set_piece_target("T_piece")
    if (random_value == 3): pieces.set_piece_target("L_piece")
    if (random_value == 4): pieces.set_piece_target("RL_piece")
    if (random_value == 5): pieces.set_piece_target("S_piece")
    if (random_value == 6): pieces.set_piece_target("Z_piece")
    if (random_value == 7): pieces.set_piece_target("Long_piece")
    if (random_value == 8): pieces.set_piece_target("Cube_piece")



def place_piece():
    for y in range(len(updating_grid.active_grid)):
        for x in range(len(updating_grid.active_grid[y])):
            if(passive_grid[y-4][x] == 0): passive_grid[y-4][x] = updating_grid.active_grid[y][x]
    randomized_piece()


def  update_and_compare_grids(piece):
    updating_grid.clear_active_grid()
    for y in range(len(updating_grid.active_grid)):
        if y == int(updating_grid.piece_pos_y):#scan and find the positon of the piece
                for piece_height in range(len(piece)):#cycle through the piece and add it to the active grid if the conditions are good
                     for piece_width in range(len(piece[piece_height])):

                        if(updating_grid.test_ground_collision(piece_height)):#add piece to the passive grid if the piece touches the ground
                            place_piece()
                        if  int(updating_grid.piece_pos_x) + piece_width < 10 and  not int(updating_grid.piece_pos_x) + piece_width < 0:
                               try:
                                   updating_grid.active_grid [int(updating_grid.piece_pos_y)+piece_height] [int(updating_grid.piece_pos_x) + piece_width] = piece[piece_height][piece_width] #add piece to the active grid
                               except IndexError:
                                   return 0 #I may plan on using this to implement a sort of gameover

                        updating_grid.test_sidewall_collision(piece_width)


def shift_rows(row):
      current_row = row
      while current_row != 0:
                for x in range(len(passive_grid[current_row])) :
                       passive_grid[current_row][x]=passive_grid[current_row-1][x]
                current_row -=1

def check_changes():
       global  score, current_piece

       #remove below line

       update_and_compare_grids(pieces.get_current_piece())

       #remove above line

       updating_grid.check_movement()
       for y in range(len(passive_grid)): #loop through the passive grid and check if each line is full then clear and shift it if it is
           count = 0
           for x in range(len(passive_grid[y])):
                 if passive_grid[y][x] != 0:
                     count += 1
                     if(count >= 10):
                       score += 100
                       shift_rows(y)
