import pygame
pygame.init()
pygame.display.set_caption('TRON')

#VARIABLES 
WIDTH = 1000
HEIGHT = 600
BORDER = 590
direction = 1

class player1: #no clue what im doing
    PLAYER = 4
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1
        #self.direction = d1

    def draw(self, color):
        global screen
        pygame.draw.rect(screen,color, (self.x, self.y), self.PLAYER)

    def update(self, color):
        global bgColor
        self.show(bgColor)

#class player2:

    #def __init__(self,x,y):
       # self.x = x
        #self.y = y
        #self.speed = 1
        #self.direction = d2
         


#playerbody
playerbody = player1(WIDTH - player1.PLAYER, HEIGHT // 2, )

#screen 
bgColor = pygame.Color("black")
fgColor = pygame.Color("yellow")
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,550,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,5,510))
pygame.draw.rect(screen, fgColor, pygame.Rect(800,40,5,515))

playerbody.draw(pygame("blue"))
print('player')


running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
