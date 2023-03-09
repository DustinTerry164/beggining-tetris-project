import pygame.image
import updating_grid,pieces
global score, falling_speed, moving_right, moving_left, current_piece,passive_grid,progress,level,game_over

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
def test_death():
    global  game_over
    for x in range(len(passive_grid[0])):
        if(passive_grid[0][x] >= 1):game_over = True
def prepare_game():
    global game_over,score,progress,level
    game_over = False
    level = 1
    progress = 0
    score = 0
def reset_game():
    global  game_over
    for y in range(len(passive_grid)):
        for x in range(len(passive_grid[y])):
            passive_grid [y] [x] = 0
    updating_grid.clear_active_grid()
    prepare_game()

def test_horizontal_collision():
    for y in range(len(passive_grid)):
        for x in range(len(passive_grid[y])):
            try:
                if updating_grid.active_grid[y+4][x] >= 1 and passive_grid[y][x+1] >= 1:
                    pieces.right_collision = True
                if updating_grid.active_grid[y+4][x] >= 1 and passive_grid[y][x-1] >= 1:
                    pieces.left_collision = True

            except IndexError:
                return 0
def test_ground_collision():
    if(int(updating_grid.piece_pos_y) == 18 - len(pieces.current_piece)): #check if the piece has hit the bottom of the screen
        place_piece()


def test_verticle_collision():
    for y in range(len(passive_grid)):
        for x in range(len(passive_grid[y])): #check if a piece is above a placed piece
            if passive_grid[y][x] >= 1 and updating_grid.active_grid[y+3][x] >= 1:
                place_piece()


def test_piece_collision(): #this function is called to test the collision of the pieces
    test_horizontal_collision()
    test_ground_collision()
    test_verticle_collision()


def place_piece():
    for y in range(len(updating_grid.active_grid)):
        for x in range(len(updating_grid.active_grid[y])):
            if(y - 4>= 0): #prevent out of bounds exception
                if(passive_grid[y-4][x] == 0):
                    passive_grid[y-4][x] = updating_grid.active_grid[y][x] #copies the entire active grid to the passive grid
    updating_grid.reset_piece()
    pieces.set_piece_target(pieces.next_piece)



def shift_rows(row):
      current_row = row
      while current_row != 0:
                for x in range(len(passive_grid[current_row])) :
                       passive_grid[current_row][x]=passive_grid[current_row-1][x]
                current_row -=1

def detect_full_line():
    global progress,level,score
    for y in range(len(passive_grid)):  # loop through the passive grid and check if each line is full then clear and shift it if it is
        count = 0
        for x in range(len(passive_grid[y])):
            if passive_grid[y][x] != 0:
                count += 1
                if (count >= 10):
                    progress += 1
                    score += 100
                    shift_rows(y)
                    if (progress >= 10):
                        progress = 0
                        level += 1
                        updating_grid.increase_difficulty()


def check_changes():
       global  current_piece

       test_death()
       updating_grid.update_grid(pieces.get_current_piece())
       test_piece_collision()
       if (updating_grid.piece_pos_y == 0): pieces.randomized_piece()  # when the piece gets reset randomize the next piece
       updating_grid.check_movement()
       detect_full_line()

