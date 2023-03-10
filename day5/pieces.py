import random
global current_piece,target_piece,piece_rotation
long_piece_pos_0 =\
    [[0],[0,3,3,3,3,0]]
long_piece_pos_1 =\
    [
    [0,3],
    [0,3],
     [0,3,0],
     [0,3]]
t_piece_pos_1 =\
    [[0,2,0],
    [0,2,2,0],
     [0,2,0]]
t_piece_pos_0 =\
    [[0,0,2,0],
    [0,2,2,2,0]]
t_piece_pos_2 =\
    [[0,0,0],
    [0,2,2,2,0],
     [0,0,2,0]]
t_piece_pos_3 =\
    [[0,0,2,0],
    [0,2,2,0],
     [0,0,2,0]]
cube_piece=\
    [[0],
    [0,3,3,0],
     [0,3,3,0]]
L_piece_pos_0=\
    [[0,1,1,0],
     [0,0,1,0],
     [0,0,1,0],]
L_piece_pos_2=\
    [[0,1,0,0],
     [0,1,0,0],
     [0,1,1,0],]
L_piece_pos_1=\
    [[0,0,0,0,0],
    [0,0,0,1,0],
     [0,1,1,1,0],]
L_piece_pos_3= \
    [[0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 1, 0, 0, 0],]
RL_piece_pos_0 =\
    [[0,2,2,0],
     [0,2,0,0],
     [0,2,0,0],]
RL_piece_pos_1= \
    [[0, 0, 0, 0, 0],
     [0, 2, 2, 2, 0],
     [0, 0, 0, 2, 0],]
RL_piece_pos_2= \
    [[0,0,2,0],
     [0,0,2,0],
     [0,2,2,0],]
RL_piece_pos_3= \
    [[0, 0, 0, 0, 0],
     [0, 2, 0, 0, 0],
     [0, 2, 2, 2, 0]]
S_piece_pos_0=\
    [[0,0,3,3,0],
     [0,3,3,0,0],]
S_piece_pos_1=\
    [[0,3,0,0],
     [0,3,3,0],
     [0,0,3,0],]
Z_piece_pos_1=\
    [[0,0,1,0],
     [0,1,1,0],
     [0,1,0,0],]
Z_piece_pos_0=\
    [[0,1,1,0,0],
     [0,0,1,1,0],]


target_piece = "RL_piece"
piece_rotation = 0 #determines rotation of piece
max_rotation = 3 #determines how many times a piece can rotate
current_piece = long_piece_pos_0

def randomized_piece():
    random_value = random.randrange(0,8,1)
    if(random_value == 0): set_piece_target("Cube_piece")
    if (random_value == 1): set_piece_target("Long_piece")
    if (random_value == 2): set_piece_target("T_piece")
    if (random_value == 3): set_piece_target("L_piece")
    if (random_value == 4): set_piece_target("RL_piece")
    if (random_value == 5): set_piece_target("S_piece")
    if (random_value == 6): set_piece_target("Z_piece")
    if (random_value == 7): set_piece_target("Long_piece")
    if (random_value == 8): set_piece_target("Cube_piece")

def rotate(direction):
    global  piece_rotation, max_rotation
    if(direction == "right"):
        piece_rotation += 1
    if(direction == "left"):
        piece_rotation -= 1
    if(piece_rotation < 0 ):
        piece_rotation = max_rotation
    if(piece_rotation > max_rotation):
        piece_rotation = 0

def set_piece_target(wanted_piece):
    global piece_rotation
    piece_rotation = 0
    global target_piece,max_rotation
    target_piece = wanted_piece

    if(wanted_piece == "T_piece"): max_rotation = 3
    if (wanted_piece == "Long_piece"): max_rotation = 1
    if (wanted_piece == "L_piece"): max_rotation = 3
    if (wanted_piece == "RL_piece"): max_rotation = 3
    if (wanted_piece == "S_piece"): max_rotation = 1
    if (wanted_piece == "Z_piece"): max_rotation = 1
    if (wanted_piece == "Cube_piece"): max_rotation = 1



def update_piece():
    global  current_piece
    if(target_piece == "T_piece"):
        if(piece_rotation == 0): current_piece = t_piece_pos_0
        if (piece_rotation == 1): current_piece = t_piece_pos_1
        if (piece_rotation == 2): current_piece = t_piece_pos_2
        if (piece_rotation == 3): current_piece = t_piece_pos_3
    if(target_piece == "Long_piece"):
        if(piece_rotation == 0): current_piece = long_piece_pos_0
        if (piece_rotation == 1): current_piece = long_piece_pos_1
    if (target_piece == "Cube_piece"): current_piece = cube_piece
    if(target_piece == "L_piece"):
        if(piece_rotation == 0): current_piece = L_piece_pos_0
        if (piece_rotation == 1): current_piece = L_piece_pos_1
        if (piece_rotation == 2): current_piece = L_piece_pos_2
        if (piece_rotation == 3): current_piece = L_piece_pos_3
    if(target_piece == "RL_piece"):
        if(piece_rotation == 0): current_piece = RL_piece_pos_0
        if (piece_rotation == 1): current_piece = RL_piece_pos_1
        if (piece_rotation == 2): current_piece = RL_piece_pos_2
        if (piece_rotation == 3): current_piece = RL_piece_pos_3
    if(target_piece == "S_piece"):
        if(piece_rotation == 0): current_piece = S_piece_pos_0
        if (piece_rotation == 1): current_piece = S_piece_pos_1
    if(target_piece == "Z_piece"):
        if(piece_rotation == 0): current_piece = Z_piece_pos_0
        if (piece_rotation == 1): current_piece = Z_piece_pos_1


def get_current_piece():
    global current_piece
    return current_piece
