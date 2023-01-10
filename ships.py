import pygame

class Ship:
    def __init__(self, pos):
        self.x, self.y = pos
        self.dir = -1"
        self.icon = pygame.image.load("invader.jpg")
    def move(self, endRow=False):
        if not endRow:
            self.x += self.dir
        else:
            self.y+=1
            self.dir *= -1

    def draw(self, win, multiplier):
            win.blit(self.icon, (self.pos[0]*multiplier, self.pos[1]*multiplier))
    
    def __str__(self):
        return "("+str(self.x)+ ", " + str(self.y)+")"

class Fleet:
    def __init__(self, size): 
        self.fleetList = [[Ship((x, y)) for x in range(size[0])] for y in range(size[1])]
        self.extraCols = 3
        self.downLast = False

    def move(self):
        if (self.fleetList[0][0].x == 0 or self.fleetList[0][0].x == len(self.fleetList[0])+self.extraCols) and not self.downLast:
            for row in self.fleetList:
                for ship in row:
                    ship.move(endRow=True)
            self.downLast = True
        else:
            for row in self.fleetList:
                for ship in row:
                    ship.move()#
            self.downLast = False
    
    def drawFleet(self, win, multiplier):
        for row in self.fleetList:
            for ship in row:
                ship.draw(win, multiplier)
            