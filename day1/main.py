import pygame
pygame.display.set_caption("Tetris _ project")
window_height = 900
window_Width = 800
background_color = (0,0,0)
Window = pygame.display.set_mode((window_Width,window_height)) #creates window for the game to run in
score = 10
pygame.font.init()
global running
running= True

box = pygame.image.load("box.png")

def display_text(text,x,y,size): #function is used for displaying white text
    font = pygame.font.Font("freesansbold.ttf",size)
    white = (255,255,255)
    text = font.render(text,True,white)
    Window.blit(text,(x,y))


def update_game():
    global  running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #terminates the game
def update_graphics():
    Window.fill(background_color)# gives the game something to draw on
    display_text("current score", window_Width - 160 , 10, 20)
    display_text(str(score), window_Width - 160, 30, 20)
    Window.blit(box,(20,20))#displays background for the stackable squares

def main():
    global running
    while running:

        update_game()
        update_graphics()

        pygame.display.update()

main()
