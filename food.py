import pygame
from pygame.locals import *
import time
import random


SIZE = 44
BACK_ROUND = (164, 233, 118)
TEXT_COL = (255, 255, 255)


class Food:
    def __init__(self, back_round):
        self.screen = back_round
        self.block = pygame.image.load("resources/food.jpg").convert()
        self.x = 132
        self.y = 132

    def draw(self):
        self.screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 15)*SIZE
        self.y = random.randint(1, 15)*SIZE
