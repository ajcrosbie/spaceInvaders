import pygame


class Ship():
    def __init__(self, pos):
        self.pos = (pos + 2) * 10

    def move(self):
        self.pos = self.pos + self.dir
        if self.pos == 0 or self.pos == 500:
            self.dir = self.dir*-1

    def draw(self, win):
        pass


class fleet():
    ships = [[][][]]

    def __init__():
        for i in range
