import pygame, sys

pygame.init()
screen_width = 750
screen_height = 1334
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))
    pygame.display.flip()
    clock.tick(60)

    ajouttest
