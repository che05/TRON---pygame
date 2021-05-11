import pygame
pygame.init()
pygame.display.set_caption('TRON')

#VARIABLES 
WIDTH = 1000
HEIGHT = 600
BORDER = 590
VELOCITY = 0.3

class player: #no clue what im doing
    PLAYER = 4
    def __init__(self,x,y,vx,vy,color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.playerColor = color
        #self.direction = d
        

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y, player.PLAYER, player.PLAYER))
    

    def update(self):
        global bgColor, VELOCITY

        nextX = self.x + self.vx
        nextY = self.y + self.vy
        

        self.show(bgColor)
        self.x = nextX
        self.y = nextY
        self.show(self.playerColor)

        
        

    def move(self,direction):
        
        print("keys")
        if direction == pygame.K_LEFT:
            self.vx = - VELOCITY
            self.vy = 0
        elif direction == pygame.K_RIGHT:
            self.vx = VELOCITY
            self.vy = 0
        elif direction == pygame.K_UP:
            self.vx = 0
            self.vy = - VELOCITY
        elif direction == pygame.K_DOWN:
            self.vx = 0
            self.vy = VELOCITY
        print("keys2")

#playerbody
player1 = player(HEIGHT // 2, HEIGHT  // 2, 2, 0,(pygame.Color('blue')))

#screen 
bgColor = pygame.Color("black")
fgColor = pygame.Color("yellow")
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,550,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,5,510))
pygame.draw.rect(screen, fgColor, pygame.Rect(800,40,5,515))

player1.show(pygame.Color('blue'))
print('player')




running = True
while running:
    pygame.display.flip()
    player1.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player1.move(event.key)
