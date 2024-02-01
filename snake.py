import time
import random
import pygame

# colors
RED = (255, 0, 0)
BackGroud = (220, 220, 220)
dot = (48, 213, 200)

pygame.init()
HEIGHT, WIDTH = 600, 400
screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption('snake')

font = pygame.font.SysFont('Impact', 30)

snake_move = 8
snake_speed = 10

clock = pygame.time.Clock()


def message(txt, color):
    text = font.render(txt, False, color)
    screen.blit(text, [HEIGHT / 2 - 100, WIDTH / 2 - 100])


def gameLoop():
    game = True
    game_close = False
    x, y = HEIGHT / 2, WIDTH / 2
    x_move, y_move = 0, 0

    snake = []
    snake_length = 1

    dot_x = round(random.randrange(0, WIDTH - snake_move) / 10.0) * 10.0
    dot_y = round(random.randrange(0, WIDTH - snake_move) / 10.0) * 10.0

    while game:

        while game_close == True:
            screen.fill(BackGroud)
            message("Змейка умерла!\nQ - выйти, Е - играть снова", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        #game = False
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_e:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_move = -snake_move
                    y_move = 0
                elif event.key == pygame.K_d:
                    x_move = snake_move
                    y_move = 0
                elif event.key == pygame.K_w:
                    y_move = -snake_move
                    x_move = 0
                elif event.key == pygame.K_s:
                    y_move = snake_move
                    x_move = 0

        if x >= HEIGHT or x < 0 or y >= WIDTH or y < 0:
            game_close = True

        x += x_move
        y += y_move
        screen.fill(BackGroud)

        pygame.draw.rect(screen, dot, [dot_x, dot_y, snake_move, snake_move])
        pygame.draw.rect(screen, RED, [x, y, snake_move, snake_move])
        pygame.display.update()
        clock.tick(snake_speed)


gameLoop()
