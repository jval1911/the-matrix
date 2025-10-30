#!/usr/bin/env python3
import pygame
import random
import sys

# Initialize
pygame.init()

# Screen setup - FULLSCREEN
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Matrix")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (200, 255, 200)

# Font - smaller for more columns
font_size = 14
font = pygame.font.Font(None, font_size)

# Matrix characters
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:,.<>?/~"

# Column setup - more columns, faster speeds
column_width = font_size
num_columns = WIDTH // column_width
columns = [random.randint(-50, 0) for _ in range(num_columns)]
speeds = [random.uniform(1.5, 3.0) for _ in range(num_columns)]

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
    
    # Fill with slight transparency for trail effect
    screen.fill(BLACK)
    
    # Draw columns
    for i in range(num_columns):
        x = i * column_width
        y = int(columns[i] * font_size)
        
        # Draw trail
        trail_length = random.randint(20, 35)
        for j in range(trail_length):
            trail_y = y - (j * font_size)
            if 0 <= trail_y < HEIGHT:
                char = random.choice(chars)
                # Fade effect
                alpha = max(0, 255 - (j * 8))
                color = (0, alpha, 0)
                text = font.render(char, True, color)
                screen.blit(text, (x, trail_y))
        
        # Draw bright head
        if 0 <= y < HEIGHT:
            char = random.choice(chars)
            text = font.render(char, True, BRIGHT_GREEN)
            screen.blit(text, (x, y))
        
        # Move column
        columns[i] += speeds[i]
        
        # Reset when off screen
        if columns[i] * font_size > HEIGHT + 100:
            columns[i] = random.randint(-20, 0)
            speeds[i] = random.uniform(1.5, 3.0)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
