import pygame
pygame.init()
pygame.display.set_caption('TRON')

#VARIABLES 
WIDTH = 1000
HEIGHT = 600
BORDER = 590
VELOCITY = 0.2

class player: #no clue what im doing
    PLAYER = 5
    def __init__(self,x,y,vx,vy,color,controls):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.playerColor = color
        self.controls = controls

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
        
        #
            if direction == self.controls[0]:
                self.vx = - VELOCITY
                self.vy = 0
            elif direction == self.controls[1]:
                self.vx = VELOCITY
                self.vy = 0
            elif direction == self.controls[2]:
                self.vx = 0
                self.vy = - VELOCITY
            elif direction == self.controls[3]:
                self.vx = 0
                self.vy = VELOCITY
        

#playerbody
player1 = player(HEIGHT // 2, HEIGHT  // 2, 0.3, 0,(pygame.Color('blue')), [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])
player2 = player(HEIGHT // 2, HEIGHT  // 2, -0.3, 0,(pygame.Color('red')), [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
#screen 
bgColor = pygame.Color("black")
fgColor = pygame.Color("yellow")
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,550,HEIGHT,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(200,40,5,510))
pygame.draw.rect(screen, fgColor, pygame.Rect(800,40,5,515))

player1.show(pygame.Color('blue'))
print('player1')
player2.show(pygame.Color('red'))
print('player2')




running = True
while running:
    pygame.display.flip()
    player1.update()
    player2.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player1.move(event.key)
            player2.move(event.key)
