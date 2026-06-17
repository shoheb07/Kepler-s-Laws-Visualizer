import pygame
import numpy as np

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Kepler's Laws Visualizer"
)

clock = pygame.time.Clock()

BLACK = (0,0,0)
YELLOW = (255,255,0)
BLUE = (100,149,237)

# Sun position
sun_x = WIDTH // 2
sun_y = HEIGHT // 2

# Ellipse parameters
a = 250
b = 180

theta = 0

running = True

while running:

    screen.fill(BLACK)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Planet position
    x = sun_x + a * np.cos(theta)
    y = sun_y + b * np.sin(theta)

    theta += 0.01

    # Orbit
    pygame.draw.ellipse(
        screen,
        BLUE,
        (
            sun_x - a,
            sun_y - b,
            2*a,
            2*b
        ),
        2
    )

    # Sun
    pygame.draw.circle(
        screen,
        YELLOW,
        (
            sun_x,
            sun_y
        ),
        20
    )

    # Planet
    pygame.draw.circle(
        screen,
        BLUE,
        (
            int(x),
            int(y)
        ),
        10
    )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
