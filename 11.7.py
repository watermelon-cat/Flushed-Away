import pygame
import random
import time
pygame.init()
Game_Screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Platformer")
Clock = pygame.time.Clock()
Game_On = True

Level_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
           [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
           [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

class enemy:
    def __init__(self, Level_2):
        self.xpos = random.randint(300, 500)
        self.ypos = 480
        self.xDir = 1
        self.health = 0
        self.speed = 1
        self.width = 64
        self.height = 32
        self.last_change_time = time.time()
        self.ratImage = pygame.image.load("rat.png").convert_alpha()
        self.ratImage = pygame.transform.scale(self.ratImage, (self.width, self.height))
        #pygame.Surface.set_colorkey (self.ratImage, [255,0,255])
        self.ratImageLeft = pygame.transform.flip(self.ratImage, 1,0)
        #self.ratImageLeft = pygame.transform.scale(self.ratImageLeft, (32, 32))
        #pygame.Surface.set_colorkey (self.ratImageLeft, [255,0,255])
        self.mapNum = Level_2
    def move(self):
        self.xpos += self.xDir*self.speed
        
        # Change direction every 3 seconds
        #if time.time() - self.last_change_time > 3:  
            #self.xDir = random.randint(-1,1)
            #self.last_change_time = time.time() #reset the time
    def collide(self):
         #right collision
        if self.mapNum[int((self.ypos) / self.height)][int((self.xpos + self.width) / self.height)] == 1:
            self.xDir*= -1
            #print("rght collision!")
        if self.mapNum[int((self.ypos) / self.height)][int((self.xpos) / self.height)] == 1 :
            self.xDir*= -1
            #print("left collision!")
    def draw(self):
        if self.xDir == 1:
            Game_Screen.blit(self.ratImage, (self.xpos, self.ypos))
        else:
            Game_Screen.blit(self.ratImageLeft, (self.xpos, self.ypos))
    
rats = []
for i in range(3):
    rats.append(enemy(Level_2))
    
LEFT= 0
RIGHT=1
UP = 2
DOWN = 3
keys = [False, False, False, False]
class Player:
    def __init__(self, mapp):
        self.xpos = 700
        self.ypos = 50
        self.height = 64
        self.width = 32
        self.vx = 0
        self.vy = 0
        self.isOnGround = False
        self.mapNum = mapp
    def move(self, keys):
        
        if keys[LEFT] == True:
            self.vx=-3
        elif keys[RIGHT] == True:
            self.vx=3
        else:
            self.vx = 0
        
        if keys[UP] and self.isOnGround == True:
            self.vy =-30
            self.isOnGround = False
            
        if keys[DOWN]:
            self.height = 32
            self.isOnGround = False
            self.collide()
        else:
            self.height = 64
        
        self.collide()
        
        
            
            
        self.xpos+=self.vx
        self.ypos+=self.vy
    def collide(self):
        if self.mapNum[int((self.ypos) / self.height)][int((self.xpos + self.width) / self.width)] == 1:
            self.xpos-= 3
            print("rght collision!")
        if self.mapNum[int((self.ypos) / self.height)][int((self.xpos) / self.width)] == 1 :
            self.xpos+= 3
            print("left collision!")
        if self.mapNum[int((self.ypos) / 32)][int((self.xpos+self.width/2)/32)] == 1:
            self.ypos += 3
            self.vy = 0
            print("up collison")
        if self.mapNum[int((self.ypos+self.height) / 32)][int((self.xpos+self.width/2) /self.width)] == 1:
            self.vy=0
            self.ypos -= 3
            self.isOnGround = True
            print("down collision!")
        else:
            self.isOnGround = False
        
        if self.isOnGround == False:
            self.vy += 3
    def draw(self):
        pygame.draw.rect(Game_Screen, (200, 0, 0), (self.xpos, self.ypos, self.width, self.height))

player = Player(Level_2)

while Game_On:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_On = False
        if event.type == pygame.KEYDOWN: #looks for key presses
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]= True
            if event.key == pygame.K_UP:
                keys[UP]=True
            if event.key == pygame.K_DOWN:
                keys[DOWN] = True
                
        elif event.type == pygame.KEYUP: #looks for key releases
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]= False
            if event.key == pygame.K_UP:
                keys[UP]=False
            if event.key == pygame.K_DOWN:
                keys[DOWN] =False
    
    player.move(keys)
            
    #physics
    for i in range(len(rats)):
        rats[i].move()
        
    for i in range(len(rats)):
        rats[i].collide()

    Game_Screen.fill((0, 0, 0))
    x = 0; y = 0
    
    for i in range(len(rats)):
        rats[i].draw()
        
    player.draw()
        
    for i in Level_2:
        for j in i:
            if j == 1:
                pygame.draw.rect(Game_Screen, (200, 200, 200), (x*32, y*32, 32, 32))
            elif j == 2 or j == 3:
                pygame.draw.rect(Game_Screen, (100, 100, 255), (x*32, y*32, 32, 32))
            x += 1
        x = 0; y += 1



    
    pygame.display.flip()
pygame.quit()


