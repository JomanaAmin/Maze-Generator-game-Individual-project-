import random
import pygame
from pygame import Rect, key
from Character import Character

from MazeGenerator import MazeGenerator
pygame.init()
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()
running = True

length=25
size=25
maze=MazeGenerator(size,length)
character=Character(maze,0,0)
screenWidth = maze.width + 200
screenHeight = maze.width + 70
screen = pygame.display.set_mode((screenWidth, screenHeight))

   # character.animate(screen)
#DIMENSIONS

screenWidth=maze.width+200
screenHeight=maze.width+70
screen = pygame.display.set_mode((screenWidth, screenHeight))


#character=pygame.draw.rect(screen,(255,255,255),(0,0,length,length),0)
font=pygame.font.Font('freesansbold.ttf',20)
text=font.render("Welcome to our maze game!", True, (0,0,0))


#BUTTONS
buttonSolveBFS=pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(maze.width + 5, 30, 190, 50))
buttonTryAgain=pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(maze.width + 5, 85, 190, 50))
buttonGenerateDFS=pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(maze.width + 5, 140, 190, 50))
buttonGenerateBFS=pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(maze.width+5, 195, 190, 50))

def drawGridPath():
    pygame.draw.line(screen,"red",(length/2,0),(length/2,length/2), 5)
    for y in range(size):
        for x in range (size):
            drawLink(maze.grid[x][y])
def drawLink(cell):
    x=cell.x
    y=cell.y
    centerX=x*length+length/2
    centerY=y*length+length/2
    if cell.links["left"]: pygame.draw.line(screen,"red",(centerX,centerY),(centerX-length,centerY),5)
    if cell.links["right"]: pygame.draw.line(screen,"red",(centerX,centerY),(centerX+length,centerY),5)
    if cell.links["top"]: pygame.draw.line(screen,"red",(centerX,centerY),(centerX,centerY-length),5)
    if cell.links["bottom"]: pygame.draw.line(screen,"red",(centerX,centerY),(centerX,centerY+length),5)

def drawGrid():
    for y in range(size):
        for x in range (size):
            drawCell(maze.grid[x][y])
def drawCell(cell):
    x=cell.x
    y=cell.y
    if cell.walls["top"]:
        pygame.draw.line(screen, (255,255,255), (x*length, y*length), ((x+1)*length, y*length))
    if cell.walls["bottom"]:
        pygame.draw.line(screen, (255,255,255), (x*length, (y+1) *length), ((x+1)*length, (y+1)*length))

    if cell.walls["left"]:
        pygame.draw.line(screen, (255,255,255), (x*length, y*length), (x*length, (y+1)*length))

    if cell.walls["right"]:
        pygame.draw.line(screen, (255,255,255), ((x+1)*length, y*length), ((x+1)*length, (y+1)*length))


def generateNewMaze(maze):

    maze.resetMaze()
    maze.DFS()


maze.resetMaze()
dfs = maze.DFS()
bfs = None
phase = "dfs"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    character.characterMovement(keys, maze)

    # Maze generation phases
    if phase == "dfs":
        try:
            next(dfs)
        except StopIteration:
            bfs = maze.BFS()
            phase = "bfs"
    elif phase == "bfs":
        try:
            next(bfs)
        except StopIteration:
            phase = "done"

    # --- DRAWING SECTION ---
    screen.fill("grey")  # Clear screen before drawing

    screen.blit(text, (screenWidth - 195, 10))  # Draw welcome text

    drawGrid()  # Draw maze walls
    if phase in ("bfs", "done"):
        drawGridPath()  # Draw path if solving is finished or in BFS

    character.animate(screen)  # Draw character sprite

    pygame.display.update()  # Refresh the display
    clock.tick(27)  # Cap FPS

pygame.quit()
