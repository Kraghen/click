import pygame
from pygame._sdl2.video import Window
import random, subprocess

pygame.init()
pygame.display.init()
pygame.font.init()

# Window setup
inf = pygame.display.Info()
w,h = 200, 150
screen = pygame.display.set_mode((w,h), pygame.NOFRAME)
pygame.display.set_caption("Catch me!")

# Drawing only once. Nothing updates
screen.fill((255, 255, 255))
pygame.display.update()

# Rendering text
font = pygame.font.SysFont("comicsansms", 20)

def add_text(text, pos, color=(0,0,0), font=font):
    render = font.render(text, True, color)
    screen.blit(render, (pos[0] - render.get_width() // 2, pos[1] - render.get_height() // 2))
    pygame.display.update()

close_text = "click to close"
text = font.render("click to close", True, (0, 0, 0))
add_text(close_text, (w//2, h//2))

# Setup moving screen
pgwindow = Window.from_display_module()
pos = (random.randint(0,inf.current_w-w), random.randint(0,inf.current_h-h))
pgwindow.position = pos

mouse = (0,0)
last_mouse = (0,0)

# Loop
clock = pygame.time.Clock()
time = 0
time_to_open_window = random.randint(120, 1200)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print("no")
            add_text("fuck", (random.randint(0, w), random.randint(0, h)))

    clock.tick(60)

    # Move
    mouse = pygame.mouse.get_pos()
    m = (-(w//2-mouse[0]), -(h//2-mouse[1]))
    
    if mouse != last_mouse:
        pos = (pos[0]-m[0], pos[1]-m[1])

    last_mouse = mouse
    pgwindow.position = pos
    
    # Open exe
    time += 1
    if time >= time_to_open_window:
        subprocess.Popen("click.exe")
        time = 0