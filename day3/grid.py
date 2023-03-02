import pygame.image
import pieces

global score, piece_pos_x, falling_speed, moving_right, moving_left, left_right_speed, current_piece
score = 0
red_cube = pygame.image.load("red_cube.png")
blue_cube = pygame.image.load("blue_cube.png")
green_cube = pygame.image.load("green_cube.png")
cubes = [red_cube,blue_cube,green_cube]
piece_pos_y = 0.0
piece_pos_x = 6.0
falling_speed = 0.1
moving_left = False
moving_right = False
left_right_speed = 0.3

# active grid will be 4 blocks taller than the passive grid
active_grid = [[0,0,0,0,0,0,0,0,0,0]
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
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]]

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
          ,[0,0,0,3,0,0,0,0,2,0]
          ,[1,2,3,3,0,0,0,0,1,3]]

def place_piece():
    global  piece_pos_y
    for y in range(len(active_grid)):
        for x in range(len(active_grid[y])):
            if(passive_grid[y-4][x] == 0): passive_grid[y-4][x] = active_grid[y][x]
    print("grid:", str(active_grid))

def  update_active_grid(piece):
    global  piece_pos_x
    clear_active_grid()
    for y in range(len(active_grid)):
        if y == int(piece_pos_y):#scan and find the positon of the piece
                for piece_height in range(len(piece)):#cycle through the piece and add it to the active grid if the conditions are good
                     for piece_width in range(len(piece[piece_height])):

                        test_ground_collision(piece_height)
                        if  int(piece_pos_x) + piece_width < 10 and  not int(piece_pos_x) + piece_width < 0:
                               try:
                                   active_grid [int(piece_pos_y)+piece_height] [int(piece_pos_x) + piece_width] = piece[piece_height][piece_width] #add piece to the active grid
                               except IndexError:
                                   print("error")
                        test_sidewall_collision(piece_width)


def test_sidewall_collision(x):
    global piece_pos_x
    if int(piece_pos_x) + x > 9:  # implement collision on the right side
        piece_pos_x -= 1
    if int(piece_pos_x) + x < 0:  # implement collision on the left side
        piece_pos_x += 1

def test_ground_collision(y):
    global piece_pos_y, falling_speed
    # print("current y", str(piece_pos_y))
    # print("current len", len(active_grid))
    if(piece_pos_y >= len(active_grid) - y ):
        print("called")

        falling_speed = 0
        place_piece()
        piece_pos_y = 0

def check_movement():
    global  piece_pos_x, piece_pos_y

    #fix movement bug after the implementation of multiple pieces
    if(moving_left):
        piece_pos_x-= left_right_speed
    if(moving_right):
        piece_pos_x += left_right_speed

def clear_active_grid():
    for y in range(len(active_grid)):
        for x in range(len(active_grid[y])):
            active_grid[y][x]=0

def shift_rows(row):
      current_row = row
      while current_row != 0:
                for x in range(len(passive_grid[current_row])) :
                       passive_grid[current_row][x]=passive_grid[current_row-1][x]
                current_row -=1

def check_changes():
       global  score, piece_pos_y, falling_speed
       piece_pos_y += falling_speed
       #remove below line
       current_piece = pieces.long_piece_pos_1
       update_active_grid(current_piece)

       check_movement()
       for y in range(len(passive_grid)):
           count = 0
           for x in range(len(passive_grid[y])):
                 if passive_grid[y][x] != 0:
                     count += 1

                     if(count >= 10):
                       score += 100
                       shift_rows(y)
