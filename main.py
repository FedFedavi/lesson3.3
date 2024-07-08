import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра_тир")
icon = pygame.image.load("image/tier.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("image/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def display_score(score):
    # Создание текста
    score_text = font.render(f"Score: {score}", True, "white")
    # Отображение текста в верхнем левом углу
    screen.blit(score_text, (10, 10))

font = pygame.font.Font(None, 74)
score = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Изменение цвета фона при каждом попадании
    display_score(score)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()


pygame.quit()