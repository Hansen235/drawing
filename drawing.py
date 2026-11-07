# instructions
print("Hello world!")
print("This is a drawing pad!")
print("Use the arrow keys to move the paintbrush!")
print("Use space to change colors!")
print("Use E to toggle eraser mode!")
print("Also, Esc exits the game.")
print("(Sorry, R is useless.)")

import pygame
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Key Drawing Pad")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

colors = [
    (255, 0, 0),
    (0, 150, 255),
    (0, 200, 80),
    (255, 200, 0),
    (180, 0, 255),
    (255, 100, 150)
]

color_index = 0
brush_color = colors[color_index]
brush_size = 8

# Drawing surface
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Starting position
x, y = WIDTH // 2, HEIGHT // 2
speed = 5

clock = pygame.time.Clock()
erasing = False

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color_index = (color_index + 1) % len(colors)
                brush_color = colors[color_index]
                erasing = False

            if event.key == pygame.K_e:
                erasing = not erasing

            if event.key == pygame.K_c:
                canvas.fill(WHITE)

            if event.key == pygame.K_ESCAPE:
                running = False

    # Arrow key movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Keep cursor inside canvas
    x = max(brush_size, min(WIDTH - brush_size, x))
    y = max(brush_size, min(HEIGHT - brush_size, y))

    # Paint
    if erasing:
        pygame.draw.circle(canvas, WHITE, (x, y), brush_size * 2)
    else:
        pygame.draw.circle(canvas, brush_color, (x, y), brush_size)

    # Display
    screen.blit(canvas, (0, 0))

    pygame.draw.circle(
        screen,
        BLACK if erasing else brush_color,
        (x, y),
        brush_size,
        1
    )

    pygame.display.flip()

pygame.quit()
sys.exit()
