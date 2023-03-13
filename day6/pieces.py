import random
global current_piece,target_piece,piece_rotation,left_collision,right_collision,next_piece
Long_piece=\
    [[0],[0,3,3,3,3,0]],\
    [
    [0,3],
    [0,3],
     [0,3,0],
     [0,3]]
T_piece =\
    [[0,0,2,0],
    [0,2,2,2,0]],\
    [[0,2,0],
    [0,2,2,0],
     [0,2,0]],\
    [[0,0,0],
    [0,2,2,2,0],
     [0,0,2,0]],\
    [[0,0,2,0],
    [0,2,2,0],
     [0,0,2,0]]

Cube_piece=\
    [[0],
    [0,3,3,0],
     [0,3,3,0]],[]
L_piece=\
    [[0,1,1,0],
     [0,0,1,0],
     [0,0,1,0],],\
    [[0,0,0,0,0],
    [0,0,0,1,0],
     [0,1,1,1,0],],\
    [[0,1,0,0],
     [0,1,0,0],
     [0,1,1,0],],\
    [[0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 1, 0, 0, 0],]
RL_piece =\
    [[0,2,2,0],
     [0,2,0,0],
     [0,2,0,0],],\
    [[0, 0, 0, 0, 0],
     [0, 2, 2, 2, 0],
     [0, 0, 0, 2, 0],], \
    [[0,0,2,0],
     [0,0,2,0],
     [0,2,2,0],],\
    [[0, 0, 0, 0, 0],
     [0, 2, 0, 0, 0],
     [0, 2, 2, 2, 0]]
S_piece=\
    [[0,0,3,3,0],
     [0,3,3,0,0],],\
    [[0,3,0,0],
     [0,3,3,0],
     [0,0,3,0],]

Z_piece=\
    [[0,0,1,0],
     [0,1,1,0],
     [0,1,0,0],],\
    [[0,1,1,0,0],
     [0,0,1,1,0],]

right_collision = False
left_collision = False
target_piece = "Long_piece"
next_piece = "Cube_piece"
piece_list_names = ["Long_piece","T_piece","Cube_piece","L_piece","RL_piece","S_piece","Z_piece"]
piece_list_object = [Long_piece,T_piece,Cube_piece,L_piece,RL_piece,S_piece,Z_piece]
piece_rotation = 0 #determines rotation of piece
max_rotation = 3 #determines how many times a piece can rotate
current_piece = Long_piece[0]

def randomized_piece():
    global next_piece
    random_value = random.randrange(0,7,1)
    next_piece = piece_list_names[random_value]
    if (random_value == 6 or random_value == 5): next_piece = piece_list_names[random_value]

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
    if (wanted_piece == "Cube_piece"): max_rotation = 0
    randomized_piece()

def update_piece():
    global  current_piece

    for x in range(len(piece_list_names)):
        if(target_piece == piece_list_names[x]):
            current_piece = piece_list_object[x][piece_rotation]
            break

def get_current_piece():
    global current_piece
    return current_p
