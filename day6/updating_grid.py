import pieces

global  piece_pos_x, piece_pos_y,falling_speed,piece_state
moving_left = False#determines if a piece is moving left
moving_right = False#determines if a piece is moving right
piece_state = 0 #determines rotation of block
left_right_speed = 0.3#determines left right movement speed of falling piece
piece_pos_y = 0.0#determines y value of falling piece
piece_pos_x = 4.0#determines x value of falling piece
falling_speed = 0.05#determines speed of falling piece

drop_speed = 0.35
target_speed = 0.05


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

def reset_piece():
    global piece_pos_x,piece_pos_y
    pieces.right_collision = False
    pieces.left_collision = False
    piece_pos_y = 0
    piece_pos_x = 4



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

def  update_grid(piece):
    clear_active_grid()
    for piece_height in range(len(piece)):#cycle through the selected piece
        for piece_width in range(len(piece[piece_height])):#cycle through the width of the piece

            if  int(piece_pos_x) + piece_width < 10 and  not int(piece_pos_x) + piece_width < 0: #only add the block to the grid if its fully on the grid
                try:
                    active_grid[int(piece_pos_y) + piece_height][int(piece_pos_x) + piece_width] = piece[piece_height][piece_width]  # add piece to the active grid
                except IndexError:
                    return 0

            test_sidewall_collision(piece_width)


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
def increase_difficulty():
    global target_speed
    target_speed = target_speed + 0.03

def check_movement():
    global  piece_pos_x, piece_pos_y

    piece_pos_y += falling_speed  # updates downward piece movement
    pieces.update_piece()

    #updates left and right movement based off keyboard actions
    if(moving_left ):
        if not pieces.left_collision:
            piece_pos_x-= left_right_speed #move the piece left if there is no block on the right
        pieces.right_collision = False #acknoledge that a piece could move right when it moves left
    if(moving_right):
        if not pieces.right_collision:
            piece_pos_x += left_right_speed #move the piece right if there is no block on the right
        pieces.left_collision = False #acknoledge that a piece could move left when it moves right
