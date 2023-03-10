import pygame
import grid, updating_grid

import pieces #imported for debugging



def  setup_window():
    global background_color, Window, window_height, window_width, running, play_area, update_rate
    pygame.display.set_caption("Tetris_project")
    window_height = 900
    window_width = 800
    background_color = (0,0,0)
    Window = pygame.display.set_mode((window_width,window_height)) #creates window for the game to run in
    pygame.font.init()
    running = True
    play_area = pygame.image.load("play_area.png")
    update_rate = pygame.time.Clock()


def display_text(text,x,y,size,color): #function is used for displaying text
    font = pygame.font.Font("freesansbold.ttf",size)
    white = (255,255,255)
    red = 255,0,0
    if color == "white" :
        text = font.render(text,True,white)
    if color == "red" :
        text = font.render(text, True, red)
    Window.blit(text,(x,y))

def monitor_keys(event):
    if event.type == pygame.KEYDOWN:#activates when key has been pressed
        if event.key ==  pygame.K_DOWN:
            print("down key has been pressed")
        if event.key == pygame.K_RIGHT:
            updating_grid.moving_right = True
        if event.key == pygame.K_LEFT:
            updating_grid.moving_left = True
        if event.key == pygame.K_v:
            pieces.rotate("right")
        if event.key == pygame.K_c:
            pieces.rotate("left")

    if event.type == pygame.KEYUP: #activates when key has been released
        if event.key == pygame.K_DOWN:
            print("down key has been released!")
        if event.key == pygame.K_RIGHT:
            updating_grid.moving_right = False
        if event.key == pygame.K_LEFT:
            updating_grid.moving_left = False


def draw_grid():
    for y in range(len(grid.passive_grid)):
        for x in range(len(grid.passive_grid[y])):
            value = grid.passive_grid[y][x]
            if value != 0:
                Window.blit(grid.cubes[value-1],((x* 60)+20,(y*60)-17))

    for y in range(len(updating_grid.active_grid)):
        for x in range(len(updating_grid.active_grid[y])):
            value = updating_grid.active_grid[y][x]
            if value != 0:
                Window.blit(grid.cubes[value-1],((x* 60)+20,(y*60)-(17 + 240)))

def update_game():
    global  running
    global update_rate
    for event in pygame.event.get():
        monitor_keys(event)
        if event.type == pygame.QUIT:
            running = False #terminates the game
    grid.check_changes()
    update_rate.tick(30)



def update_graphics():
    Window.fill(background_color)# gives the game something to draw on
    display_text("current score", window_width - 160 , 10, 20,"white")
    display_text(str(grid.score), window_width - 160, 30, 20,"white")
    Window.blit(play_area,(20,20))#displays background for the stackable squares
    draw_grid()
    pygame.display.update()

def main():
    setup_window()
    pieces.set_piece_target("S_piece")
    while running:
        update_game()
        update_graphics()

main()
