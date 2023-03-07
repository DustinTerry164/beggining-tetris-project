import pieces

global  piece_pos_x, piece_pos_y,falling_speed,piece_state
moving_left = False
moving_right = False
piece_state = 0 #determines rotation of block
left_right_speed = 0.3#determines left right movement speed of falling piece
piece_pos_y = 0.0#determines y value of falling piece
piece_pos_x = 4.0#determines x value of falling piece
falling_speed = 0.07#determines speed of falling piece

drop_speed = 0.35
target_speed = 0.07


# active grid will be 4 blocks taller than the passive grid
#active grid is 18 blocks tall
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


def increase_drop_speed():
    global  falling_speed
    falling_speed = drop_speed + target_speed

def reset_drop_speed():
    global falling_speed
    falling_speed = target_speed

def clear_active_grid():
    for y in range(len(active_grid)):
        for x in range(len(active_grid[y])):
            active_grid[y][x]=0

def test_sidewall_collision(x):
    global moving_left,moving_right,piece_pos_x
    if int(piece_pos_x) + x > 9:  # implement collision on the right side
        moving_right = False
        if int(piece_pos_x) + x == 11:#stop players from glitching the pieces into the walls
            piece_pos_x -= 1
    if int(piece_pos_x) < -1:  # implement collision on the left side
        moving_left = False
        if int(piece_pos_x) + x == -2:#stop players from glitching the pieces into the walls
            piece_pos_x += 1

def check_movement():
    global  piece_pos_x, piece_pos_y
    piece_pos_y += falling_speed  # updates downward piece movement
    pieces.update_piece()

    #updates left and right movement based off keyboard actions
    if(moving_left):
        piece_pos_x-= left_right_speed
    if(moving_right):
        piece_pos_x += left_right_speed
