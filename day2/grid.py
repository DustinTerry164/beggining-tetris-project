import pygame.image
global score
score = 0
red_cube = pygame.image.load("red_cube.png")
blue_cube = pygame.image.load("blue_cube.png")
green_cube = pygame.image.load("green_cube.png")
cubes = [red_cube,blue_cube,green_cube]


grid = [[0,0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,0,0,0,0,0,0,0,0,0]
          ,[0,3,0,0,0,0,0,0,0,0]
          ,[3,3,3,3,3,3,3,2,0,2]
          ,[0,1,1,0,0,0,0,0,0,0]
          ,[2,1,3,1,2,0,2,2,2,2]
          ,[1,1,1,2,2,0,3,2,2,2]]

def shift_rows(row):
      current_row = row
      while current_row != 0:
                for x in range(len(grid[current_row])) :
                       grid[current_row][x]=grid[current_row-1][x]
                current_row -=1

def check_changes():
       global  score
       for y in range(len(grid)):
           count = 0
           for x in range(len(grid[y])):
                 if grid[y][x] != 0:
                     count += 1
                     if(count == 10):
                       score += 10
                       shift_rows(y)
