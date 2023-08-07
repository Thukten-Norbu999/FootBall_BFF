import pygame as pg
import math, random
import time

pg.init()

WIDTH, HEIGHT = 500, 500
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
DARK_GREEN = (0,100,0)
BLUE = (0,0,255)
LIGHT_BLUE = (200,200,255)

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('GAME')

class Character:
    def __init__(self, height, on_platform,isJumping, x,y):
        self.height = height
        self.on_platform = on_platform
        self.isJumping = isJumping
        self.x = x
        self.y = y

    def draw(self):
        pg.draw.rect(WIN, BLACK, (self.x, self.y, 20, self.height))

class Platform:
    def __init__(self, x, y):
        self.y = y
        self.x = x
    
    def draw(self):
        pg.draw.rect(WIN, GREEN, (self.x, self.y, random.randint(150,300), 20))
        
        # if self.x < 10:
        #     pass
        # else:
        #     pg.draw.rect(WIN, GREEN, (self.x, self.y, random.randint(150,300), 20))
        #     self.draw()

# def redraw(x):
#     if x < 10:
#         pt.draw(x)
#     else:
#         pt.draw(pt.x)
    

frequency = 45/(2*math.pi)
pivot_x, pivot_y = WIDTH/2, HEIGHT/2

pt_x , pt_y = 800, random.randint(WIDTH/2, 400)
person = Character(30, False , False, 10, 400)
pt = Platform(pt_x, pt_y)
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    person.y -= 35
                elif event.key == pg.K_RIGHT:
                    person.x += 10
                elif event.key == pg.K_LEFT:
                    person.x -= 10
    
    print('WIN')
 
    WIN.fill(LIGHT_BLUE)

    x = pivot_x+(math.pi/4)*100*math.cos(math.pi*frequency*time.time())
    y = pivot_y+(math.pi/4)*100*math.sin(math.pi*frequency*time.time())
    
    
    
    if (person.y == pt.y and (person.x == pt.x)):
        print(True)
    else:
        if person.y < 420:
            person.y += .098
        
    print(pt.x)
    if pt.x < 10:
        pt.x = random.randint(500,800)
        pt.draw()
        
    else:
        pt.x -= .5
        pt.draw()

    


    pg.draw.rect(WIN, DARK_GREEN, (0,450, 500, 50))
    person.draw()
    
    
    
    #pg.draw.rect(WIN, BLUE, (x, y, 20, 10))
    
    pg.display.update()

pg.quit()