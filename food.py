import pygame
from pygame.locals import *
import time
import random


SIZE = 44
BACK_ROUND = (225, 145, 238)
TEXT_COL = (225, 145, 238)


class Food:
    def __init__(self, back_round):
        self.screen = back_round
        arch = open('food_type', 'r')
        comida = arch.readline()
        arch.close()
        if comida[0] == 'a':
            comida = "apple"
        if comida[0] == 'h':
            comida = "food"
        if comida[0] == 'p':
            comida = "pizza"
        self.block = pygame.image.load(str("resources/" + comida + ".png")).convert_alpha()
        self.x = 132
        self.y = 132

    def draw(self):
        self.screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def collides(self, x1, y1, x2, y2):
        if x2 <= x1 < x2+SIZE and y2 <= y1 < y2 + SIZE:
            return True
        else:
            return False

    def move(self, n, snake_x, snake_y):
        ok = False
        while not ok:
            self.x = random.randint(1, 15)*SIZE
            self.y = random.randint(1, 15)*SIZE
            good = True
            for i in range(n):
                if i < n and self.collides(self.x, self.y, snake_x[i], snake_y[i]):
                    good = False
                    break

            if good:
                ok = True
