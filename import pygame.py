import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define the Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 50]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
    
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(window, black, element, self.radius)
    
    def move(self):
        for i in range(len(self.elements)-1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
    
    def add_element(self):
        self.size += 1
        self.elements.append([0, 0])
    
    def reset(self):
        self.size = 1
        self.elements = [[100, 50]]
        self.radius = 10
        self.dx = 5
        self.dy = 0

# Define the Food class
class Food:
    def __init__(self):
        self.position = [random.randrange(0, window_width-10, 10), random.randrange(0, window_height-10, 10)]
        self.radius = 5
    
    def draw(self):
        pygame.draw.circle(window, red, self.position, self.radius)

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Define the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dx = -5
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = 5
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -5
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 5
    
    # Move the Snake
    snake.move()
    
    # Check for collision with Food
    if abs(snake.elements[0][0] - food.position[0]) < 10 and abs(snake.elements[0][1] - food.position[1]) < 10:
        snake.add_element()
        food = Food()
    
    # Check for collision with walls
    if snake.elements[0][0] < 0 or snake.elements[0][0] > window_width or snake.elements[0][1] < 0 or snake.elements[0][1] > window_height:
        snake.reset()
    
    # Check for collision with self
    for element in snake.elements[1:]:
        if abs(snake.elements[0][0] - element[0]) < 10 and abs(snake.elements[0][1] - element[1]) < 10:
            snake.reset()
    
    # Draw the game objects
    window.fill(white)
    snake.draw()
    food.draw()
    pygame.display.update()
    
    # Set the game clock
    clock.tick(30)

# Quit Pygame
pygame.quit()
