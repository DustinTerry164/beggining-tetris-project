import pygame
import grid



def  setup_window():
    global background_color, Window, window_height, window_width, running, box
    pygame.display.set_caption("Tetris_project")
    window_height = 900
    window_width = 800
    background_color = (0,0,0)
    Window = pygame.display.set_mode((window_width,window_height)) #creates window for the game to run in
    pygame.font.init()
    running = True
    box = pygame.image.load("box.png")


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
            grid.grid[12][5] = 1
            print("key has been pressed")

    if event.type == pygame.KEYUP: #activates when key has been released
        if event.key == pygame.K_DOWN:
            print("key has been released!")


def draw_grid():
    for y in range(len(grid.grid)):
        for x in range(len(grid.grid[y])):
            value = grid.grid[y][x]
            if value != 0:
                Window.blit(grid.cubes[value-1],((x* 60)+20,(y*60)-17))

def update_game():
    global  running
    for event in pygame.event.get():
        monitor_keys(event)
        grid.check_changes()
        if event.type == pygame.QUIT:
            running = False #terminates the game

def update_graphics():
    Window.fill(background_color)# gives the game something to draw on
    display_text("current score", window_width - 160 , 10, 20,"white")
    display_text(str(grid.score), window_width - 160, 30, 20,"white")
    Window.blit(box,(20,20))#displays background for the stackable squares
    draw_grid()
    pygame.display.update()

def main():
    setup_window()
    while running:
        update_game()
        update_graphics()

main()
