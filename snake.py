import random
import pygame

pygame.init()
# colors
RED = (255, 0, 0)
BackGround = (220, 220, 220)
dot = (0, 0, 200)

HEIGHT, WIDTH = 600, 400
screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption('snake')

clock = pygame.time.Clock()

snake_move = 10
snake_speed = 10

font = pygame.font.SysFont('Impact', 20)


def its_snake(snake_move, snake):
    for i in snake:
        pygame.draw.rect(screen, RED, [i[0], i[1], snake_move, snake_move])


def message(txt, color):
    text = font.render(txt, False, color)
    screen.blit(text, [HEIGHT / 5, WIDTH / 3])


def score(score):
    value = font.render("Score: " + str(score), False, (0, 0, 0))
    screen.blit(value, [0, 0])


def final_score(score):
    value = font.render("Score: " + str(score), False, (0, 0, 0))
    screen.blit(value, [HEIGHT / 2 - 40, WIDTH / 3 + 80])
    return value


def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')


def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))


def print_record(record):
    value = font.render("record: " + str(record), False, (0, 0, 0))
    screen.blit(value, [HEIGHT / 2 - 45, WIDTH / 3 + 40])


def gameLoop():
    record = get_record()
    game = True
    game_close = False

    x, y = HEIGHT / 2, WIDTH / 2
    x_move, y_move = 0, 0

    snake = []
    snake_length = 1

    dot_x = round(random.randrange(0, HEIGHT - snake_move) / 10.0) * 10.0 - 10
    dot_y = round(random.randrange(0, WIDTH - snake_move) / 10.0) * 10.0 - 10

    while game:

        while game_close == True:
            screen.fill(BackGround)
            message("Змейка умерла!  Q - выйти, Е - играть снова", RED)
            final_score(snake_length - 1)
            set_record(record, snake_length - 1)
            print_record(record)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
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
        screen.fill(BackGround)

        pygame.draw.rect(screen, dot, [dot_x, dot_y, snake_move, snake_move])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        for i in snake[:-1]:
            if i == snake_head:
                game_close = True

        its_snake(snake_move, snake)
        score(snake_length - 1)

        pygame.display.update()

        if x == dot_x and y == dot_y:
            dot_x = round(random.randrange(0, HEIGHT - snake_move) / 10.0) * 10.0
            dot_y = round(random.randrange(0, WIDTH - snake_move) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    quit()

gameLoop()
