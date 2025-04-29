
import pygame
import random
from config import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.reset()
        self.size = TILE_SIZE
        self.body = [
            [5 * TILE_SIZE, 5 * TILE_SIZE],  
            [4 * TILE_SIZE, 5 * TILE_SIZE], 
            [3 * TILE_SIZE, 5 * TILE_SIZE],  
        ]
        self.direction = (1, 0)  

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = [head_x + dir_x * self.size, head_y + dir_y * self.size]
        self.body.insert(0, new_head) 
        self.body.pop()

    def reset(self):
        self.snake = [(100, 100)] 
        self.direction = (GRID_SIZE, 0)
        self.food = self.random_food()
        self.score = 0

    def random_food(self):
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return (x, y)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, GRID_SIZE):
                    self.direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and self.direction != (0, -GRID_SIZE):
                    self.direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and self.direction != (GRID_SIZE, 0):
                    self.direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-GRID_SIZE, 0):
                    self.direction = (GRID_SIZE, 0)

    def update(self):
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        
       
        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in self.snake
        ):
            self.reset()
            return

        self.snake.insert(0, head) 
        if head == self.food: 
            self.food = self.random_food() 
            self.score += 1
        else:
            self.snake.pop()

    def draw(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, NEON_GREEN, (*segment, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(self.screen, NEON_PINK, (*self.food, GRID_SIZE, GRID_SIZE))