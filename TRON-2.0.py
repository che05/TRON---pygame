import pygame, time
pygame.init()
pygame.display.set_caption('TRON')

#VARIABLES 
WIDTH = 600
HEIGHT = 500
BORDER = 580
VELOCITY = 1


class player: #no clue what im doing
    PLAYER = 5
    def __init__(self,name,x,y,vx,vy,color,controls,tail):
        self.name = name
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.playerColor = color
        self.controls = controls
        self.tail = tail

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y, player.PLAYER, player.PLAYER))
    
    def update(self,opponentTail):
        global bgColor, VELOCITY, nextX, nextY

        self.tail.append((self.x, self.y))

        nextX = self.x + self.vx
        nextY = self.y + self.vy

        if (nextX, nextY) in self.tail:
            print(self.name + " stop hitting yourself.")
            running == False
        elif (nextX, nextY) in opponentTail:
            print(" stop hitting your opponent!")
            running == False
        if nextX < 10 or nextX > WIDTH - 10
            print(self.name + " hit the left or right wall.")
            screen.fill("black")
            
        if nextY < 10 or nextY > HEIGHT - 10:
            print(self.name + " hit the top or bottom wall.")
            
               
        #self.show(bgColor)
        self.x = nextX
        self.y = nextY
        self.show(self.playerColor)

    def move(self,direction):
        
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

    def new_game():
        newP1 = player("blue", HEIGHT // 2 - 200, HEIGHT  // 2, 1, 0,(pygame.Color('blue')), [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s], [])
        newP2 = player("red", HEIGHT // 2 + 300, HEIGHT  // 2, -1, 0,(pygame.Color('red')), [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN], [])

    def endGame(self):
        running == False
        
        
gameSpeed = pygame.time.Clock()
#playerbody
player1 = player("blue", HEIGHT // 2 - 200, HEIGHT  // 2, 1, 0,(pygame.Color('blue')), [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s], [])
player2 = player("red", HEIGHT // 2 + 300, HEIGHT  // 2 , -1, 0,(pygame.Color('red')), [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN], [])
#screen 
bgColor = pygame.Color("black")
fgColor = pygame.Color("yellow")
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.draw.rect(screen, fgColor, pygame.Rect(5,10,BORDER,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(5,495,BORDER,5))
pygame.draw.rect(screen, fgColor, pygame.Rect(5,10,5,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(585,10,5,BORDER))
    
player1.show(pygame.Color('blue'))
print('player1')
player2.show(pygame.Color('red'))
print('player2')

display_surface = pygame.display.set_mode((200, 40))
textRect.center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    pygame.display.flip()
    gameSpeed.tick(120)
    player1.update(player2.tail)
    player2.update(player1.tail)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player1.move(event.key)
            player2.move(event.key)
        
