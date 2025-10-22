import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

x, y = 50, 300
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 80))

    x += speed
    if x > 750:
        x = 50

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
