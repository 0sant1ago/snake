import pygame
from pygame.locals import *
import time
import random
from snake import Snake
from food import Food

SIZE = 44
BACK_ROUND = (164, 233, 118)
TEXT_COL = (255, 255, 255)


class Game:
    def __init__(self):
        pygame.init()
        self.back_round = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.back_round)
        self.snake.draw()
        self.food = Food(self.back_round)
        self.food.draw()

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.back_round.blit(img, (x, y))

    def collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2+SIZE and y2 <= y1 < y2 + SIZE:
            return True
        else:
            return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.back_round.blit(score, (850, 10))

    def reset(self):
        self.snake = Snake(self.back_round)
        self.food = Food(self.back_round)

    def show(self):
        self.snake.walk()
        self.food.draw()
        self.display_score()
        pygame.display.flip()

        # snake eats hamburger
        if self.collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.increase_length()
            self.food.move()

        # snake hits itself
        for i in range(2, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"

        # snake hits the boundaries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            # self.play_sound('crash')
            raise "Hit the boundary"

    def start(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        pause = False

                    if not pause:

                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.show()

            except Exception as error:
                self.game_over()
                pause = True
                self.reset()

            time.sleep(.2)

    def game_over(self):
        self.back_round.fill(BACK_ROUND)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.back_round.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.back_round.blit(line2, (200, 350))

        pygame.display.flip()
        time.sleep(2)
