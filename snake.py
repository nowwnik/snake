import pygame

#colors
RED = (255, 0, 0)
BackGroud = (220, 220, 220)
dot = (48, 213, 200)

pygame.init()
HEIGHT, WEIGHT = 600, 400
screen = pygame.display.set_mode((HEIGHT, WEIGHT))

pygame.display.set_caption('snake')

font = pygame.font.SysFont(None,25)

x, y = HEIGHT/2, WEIGHT/2

x_move, y_move = 0, 0

snake_move = 8
snake_speed = 15

def message (txt, color):
    text = font.render(txt,False,color)
    screen.blit(text, (HEIGHT/2,WEIGHT/2 ))

clock = pygame.time.Clock()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x_move = -10
                y_move = 0
            elif event.key == pygame.K_d:
                x_move = 10
                y_move = 0
            elif event.key == pygame.K_w:
                y_move = -10
                x_move = 0
            elif event.key == pygame.K_s:
                x_move = 10
                y_move = 0
    x += x_move
    y += y_move
    screen.fill(BackGroud)

    pygame.draw.rect(screen, RED, [x, y, 8, 8])
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
