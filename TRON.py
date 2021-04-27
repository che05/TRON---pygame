import pygame
pygame.init()
pygame.display.set_caption('TRON')

#VARIABLES 
WIDTH = 1000
HEIGHT = 600
BORDER = 590

#screen 
bgColor = pygame.Color("black")
fgColor = pygame.Color("yellow")
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,550,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,5,510))
pygame.draw.rect(screen, fgColor, pygame.Rect(800,40,5,515))

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
