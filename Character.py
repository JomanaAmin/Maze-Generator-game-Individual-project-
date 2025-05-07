
import pygame
class Character:
    def __init__(self, maze,x,y):
        self.maze = maze
        self.x=x
        self.y=y
        self.vel=maze.length/2
        self.direction={
            "up":False,
            "down":False,
            "left":False,
            "right":False
        }
        self.walkRight = [
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\right\right1.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\right\right2.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\right\right3.png")
        ]

        self.walkLeft = [
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\left\left1.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\left\left2.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\left\left3.png")
        ]

        self.walkUp = [
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\up\up1.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\up\up2.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\up\up3.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\up\up4.png")
        ]

        self.walkDown = [
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\down\down1.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\down\down2.png"),
            pygame.image.load(r"Y:\AlgoProject\ezgif-split\down\down3.png")
        ]
        self.idle=pygame.image.load(r"Y:\AlgoProject\ezgif-split\idle\idle1.png")

       # self.topLeftCorner=(self.x,self.y)
       # self.topRightCorner=(self.x,self.y+length)
       # self.bottomLeftCorner=(self.x+length,self.y)
       # self.bottomRightCorner=(self.x+length,self.y+length)
       # self.currentCell=(x,y)
        self.walkCount=0
    def canPass(self,maze,key):
        currCellX = int(self.x // maze.length)
        currCellY = int(self.y // maze.length)
        if key[pygame.K_LEFT]:
            nextCellX=currCellX-1
            nextCellY=currCellY
        elif key[pygame.K_RIGHT]:
            nextCellX=currCellX+1
            nextCellY=currCellY
        elif key[pygame.K_UP]:
            nextCellX=currCellX
            nextCellY=currCellY-1
        elif key[pygame.K_DOWN]:
            nextCellX = currCellX
            nextCellY = currCellY+1
        nextCell=maze.grid[nextCellX][nextCellY]
        currCell=maze.grid[currCellX][currCellY]
        return maze.thereIsPath(currCell,nextCell)
    def animate(self,screen):
        if self.walkCount>=26:
            self.walkCount=0
        if self.direction["up"]:
            screen.blit(self.walkUp[self.walkCount//3],(self.x,self.y))
        if self.direction["down"]:
            screen.blit(self.walkDown[self.walkCount//3],(self.x,self.y))
        if self.direction["left"]:
            screen.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
        if self.direction["right"]:
            screen.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
        else:
            screen.blit(self.idle,(self.x,self.y))

    def characterMovement(self,keys,maze):
        if keys[pygame.K_LEFT] and self.x >= maze.length / 2 and self.canPass(maze,keys):
            self.direction["left"] = True
            self.direction["right"] = False
            self.direction["up"] = False
            self.direction["down"] = False
            self.x -= self.vel
        elif keys[pygame.K_RIGHT] and self.x <= maze.width - maze.length and self.canPass(maze,keys):
            self.direction["right"] = True
            self.direction["left"] = False
            self.direction["up"] = False
            self.direction["down"] = False
            self.x += self.vel
        elif keys[pygame.K_UP] and self.x >= maze.length and self.canPass(maze,keys):
            self.direction["up"] = True
            self.direction["left"] = False
            self.direction["right"] = False
            self.direction["down"] = False
            self.y -= self.vel
        elif keys[pygame.K_DOWN] and self.x <= maze.width and self.canPass(maze,keys):
            self.direction["down"] = True
            self.direction["left"] = False
            self.direction["right"] = False
            self.direction["up"] = False
            self.y += self.vel
        else:
            self.direction["left"] = False
            self.direction["right"] = False
            self.direction["up"] = False
            self.direction["down"] = False
            self.walkCount = 0

