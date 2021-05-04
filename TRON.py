import pygame
pygame.init()
pygame.display.set_caption('TRON')

#VARIABLES 
WIDTH = 1000
HEIGHT = 600
BORDER = 590
VELOCITY = 1

class player: #no clue what im doing
    PLAYER = 4
    def __init__(self,x,y,vx,vy,):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.speed = 1
        #self.direction = d
        

    def show(self, color):
        global screen
        pygame.draw.rect(screen,color, pygame.Rect(self.x,self.y, player.PLAYER, player.PLAYER))
    

    def update(self, color):
        global bgColor
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(color)

    def move(self):
        if self.x <=0:
            self.x += self.direction[0]
            self.y += self.direction[1]
        else:
            self.x += self.direction[0] * 2
            self.y += self.direction[1] * 2


#playerbody
player1 = player(HEIGHT // 2, HEIGHT  // 2, (2,0), 1)

#screen 
bgColor = pygame.Color("black")
fgColor = pygame.Color("yellow")
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,550,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,5,510))
pygame.draw.rect(screen, fgColor, pygame.Rect(800,40,5,515))

player1.show(pygame.Color('white'))
print('player')


#keys=pygame.key.get_pressed()
#if keys[K_LEFT]:
#    direction-=1
#    if direction==-1:
#        direction=0
#if keys[K_RIGHT]:
#    direction+=1
#    if direction==5:
#        direction=4    
#if keys[K_UP]:
#    direction

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
