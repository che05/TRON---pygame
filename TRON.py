import pygame
pygame.init()
pygame.display.set_caption('TRON')

#VARIABLES 
WIDTH = 1200
HEIGHT = 600

#screen 
screen = pygame.dislpay.set_mode((WIDTH, HEIGHT))

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygmae.QUIT:
            running = False