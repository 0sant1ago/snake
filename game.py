import pygame, sys
from pygame.locals import *
import time
import random
from snake import Snake
from food import Food
from pygame import mixer

SIZE = 44
BACK_ROUND = (211, 102, 228)
TEXT_COL = (211, 102, 228)


class Game:
    def __init__(self, time_difficulty):
        pygame.init()
        self.time_difficulty = time_difficulty
        self.back_round = pygame.display.set_mode((1000, 704))
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
            eating_sound = mixer.Sound("snake_eating.wav")
            eating_sound.play()
            self.snake.increase_length()
            self.food.move(self.snake.length, self.snake.x, self.snake.y)

        # snake hits itself
        for i in range(2, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                explosion_sound = mixer.Sound("explosion.wav")
                explosion_sound.play()
                raise "Collision Occurred"

        # snake hits the boundaries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 700):
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
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

            time.sleep(self.time_difficulty)
            # time.sleep(.2)

        pygame.quit()
        sys.exit()

    def game_over(self):
        font = pygame.font.SysFont('arial', 60)
        line1 = font.render(f"Game is over! Your score is:  {self.snake.length}", True, (255, 255, 255))
        self.back_round.blit(line1, (200, 200))
        line2 = font.render("To play again press Enter.", True, (255, 255, 255))
        self.back_round.blit(line2, (200, 350))
        #lin3 3 = to   falta boton para regresar al menu

        # ahora actualizar el archivo de highest_scores
        arch = open('highest_scores.txt', 'r')
        scores = list()
        while True:
            cadena = arch.readline()
            if not cadena:
                break
            scores.append(cadena)
        arch.close()

        scores.append(self.snake.length)
        for i in range(len(scores)):
            scores[i] = int(scores[i])

        scores.sort()
        scores.reverse()

        arch = open('highest_scores.txt', 'w')
        for i in scores:
            arch.write(str(i))
            arch.write('\n')
        arch.close()

        pygame.display.flip()
        time.sleep(2)
