import pygame
from pygame.locals import *
import time
import random

SIZE = 44
BACK_ROUND = (225, 145, 238)
TEXT_COL = (225, 145, 238)


class Snake:
    def __init__(self, back_round):
        self.screen = back_round

        arch = open('snake_type', 'r')
        color_snake = arch.readline()
        arch.close()
        if color_snake[0] == 'g':
            color_snake = "block"
        if color_snake[0] == 'y':
            color_snake = "block2"

        self.block = pygame.image.load(str("resources/" + color_snake + ".jpg")).convert()

        #self.block = pygame.image.load("resources/block.jpg").convert()

        self.direction = 'down'
        self.length = 1
        self.x = [SIZE] * self.length
        self.y = [SIZE] * self.length

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def draw(self):
        self.screen.fill(BACK_ROUND)

        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
