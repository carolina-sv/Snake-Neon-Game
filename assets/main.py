
import pygame
from game import Game
from config import *

import pygame

pygame.init()
pygame.mixer.init()  

pygame.mixer.music.load("songs/theme.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Neon")
clock = pygame.time.Clock()

game = Game(screen)

running = True
while running:
    screen.fill(BLACK)
    game.handle_events()
    game.update()
    game.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

from config import BLACK,WIDTH, HEIGHT, FPS
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


while True:
    screen.fill(BLACK)
    

    pygame.display.update()
    clock.tick(FPS)
