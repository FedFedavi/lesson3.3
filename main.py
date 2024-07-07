import pygame

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("image/tier.jpg")

running = True
while running:
    pass

pygame.quit()