import pygame, sys
from button import Button
from game import Game

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("resources/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("resources/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Choose the difficulty.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 660),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_EASY = Button(image=None, pos=(640, 260),
                           text_input="EASY", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_EASY.changeColor(PLAY_MOUSE_POS)
        PLAY_EASY.update(SCREEN)

        PLAY_NORMAL = Button(image=None, pos=(640, 360),
                             text_input="NORMAL", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_NORMAL.changeColor(PLAY_MOUSE_POS)
        PLAY_NORMAL.update(SCREEN)

        PLAY_HARD = Button(image=None, pos=(640, 460),
                           text_input="HARD", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_HARD.changeColor(PLAY_MOUSE_POS)
        PLAY_HARD.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_EASY.checkForInput(PLAY_MOUSE_POS):
                    game = Game(0.2)
                    game.start()
                if PLAY_NORMAL.checkForInput(PLAY_MOUSE_POS):
                    game = Game(0.15)
                    game.start()
                if PLAY_HARD.checkForInput(PLAY_MOUSE_POS):
                    game = Game(0.1)
                    game.start()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(45).render("OPTIONS", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_RECORDS = Button(image=None, pos=(640, 320),
                                 text_input="HIGHEST SCORES", font=get_font(50), base_color="White",
                                 hovering_color="Green")

        OPTIONS_RECORDS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_RECORDS.update(SCREEN)

        OPTIONS_CHANGEFOOD = Button(image=None, pos=(640, 180),
                                    text_input="CHANGE TYPE OF FOOD", font=get_font(50),
                                    base_color="White", hovering_color="Green")

        OPTIONS_CHANGEFOOD.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_CHANGEFOOD.update(SCREEN)

        OPTIONS_CHANGESNAKE = Button(image=None, pos=(640, 480),
                                     text_input="CHANGE COLOR OF SNAKE", font=get_font(50),
                                     base_color="White", hovering_color="Green")

        OPTIONS_CHANGESNAKE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_CHANGESNAKE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_RECORDS.checkForInput(OPTIONS_MOUSE_POS):
                    show_records()
                if OPTIONS_CHANGEFOOD.checkForInput(OPTIONS_MOUSE_POS):
                    change_food()
                if OPTIONS_CHANGESNAKE.checkForInput(OPTIONS_MOUSE_POS):
                    change_snake()

        pygame.display.update()


def change_snake():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        GREEN = Button(image=None, pos=(640, 300),
                       text_input="Green", font=get_font(75), base_color="White", hovering_color="Green")
        GREEN.changeColor(OPTIONS_MOUSE_POS)
        GREEN.update(SCREEN)

        YELLOW = Button(image=None, pos=(640, 400),
                       text_input="Yellow", font=get_font(75), base_color="White", hovering_color="Green")
        YELLOW.changeColor(OPTIONS_MOUSE_POS)
        YELLOW.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options()
                if GREEN.checkForInput(OPTIONS_MOUSE_POS):
                    arch = open('snake_type', 'w')
                    arch.write("green")
                    arch.close()
                    main_menu()
                if YELLOW.checkForInput(OPTIONS_MOUSE_POS):
                    arch = open('snake_type', 'w')
                    arch.write("yellow")
                    arch.close()
                    main_menu()

        pygame.display.update()


def change_food():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        APPLE = Button(image=None, pos=(640, 100),
                       text_input="Apple", font=get_font(75), base_color="White", hovering_color="Green")

        APPLE.changeColor(OPTIONS_MOUSE_POS)
        APPLE.update(SCREEN)

        HAMBURGER = Button(image=None, pos=(640, 220),
                           text_input="Hamburger", font=get_font(75), base_color="White", hovering_color="Green")

        HAMBURGER.changeColor(OPTIONS_MOUSE_POS)
        HAMBURGER.update(SCREEN)

        PIZZA = Button(image=None, pos=(640, 330),
                       text_input="Pizza", font=get_font(75), base_color="White", hovering_color="Green")

        PIZZA.changeColor(OPTIONS_MOUSE_POS)
        PIZZA.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options()
                if APPLE.checkForInput(OPTIONS_MOUSE_POS):
                    arch = open('food_type', 'w')
                    arch.write("apple")
                    arch.close()
                    main_menu()
                if HAMBURGER.checkForInput(OPTIONS_MOUSE_POS):
                    arch = open('food_type', 'w')
                    arch.write("hamburger")
                    arch.close()
                    main_menu()
                if PIZZA.checkForInput(OPTIONS_MOUSE_POS):
                    arch = open('food_type', 'w')
                    arch.write("pizza")
                    arch.close()
                    main_menu()

        pygame.display.update()


def show_records():
    arch = open('highest_scores.txt', 'r')
    con = 0
    pos = list()
    while True:
        cadena = arch.readline()
        if not cadena:
            break
        if con == 3:
            break
        pos.append(cadena)
        con += 1
    arch.close()

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        first, second, third = 'None', 'None', 'None'
        if con == 3:
            first, second, third = pos[0], pos[1], pos[2]
            first = first[0:len(first) - 1]
            second = second[0:len(second) - 1]
            third = third[0:len(third) - 1]
        if con == 2:
            first, second = pos[0], pos[1]
            first = first[0:len(first) - 1]
            second = second[0:len(second) - 1]
        if con == 1:
            first = pos[0]
            first = first[0:len(first) - 1]

        FIRST_TEXT = get_font(45).render("1. " + first + " points", True, "White")
        FIRST_RECT = FIRST_TEXT.get_rect(center=(640, 80))
        SCREEN.blit(FIRST_TEXT, FIRST_RECT)

        SECOND_TEXT = get_font(45).render("2. " + second + " points", True, "White")
        SECOND_RECT = SECOND_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(SECOND_TEXT, SECOND_RECT)

        THIRD_TEXT = get_font(45).render("3. " + third + " points", True, "White")
        THIRD_RECT = THIRD_TEXT.get_rect(center=(640, 240))
        SCREEN.blit(THIRD_TEXT, THIRD_RECT)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("resources/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("resources/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("resources/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
