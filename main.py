import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

footballer = Actor("footballer")
footballer.pos = 100,100

football = Actor("football")
football.pos = 200,200

def draw():
    screen.blit("background", (0,0))
    football.draw()
    footballer.draw()
    screen.draw.text("Score: "+ str(score), color="black", topleft=(10,10))

    if game_over:
            screen.fill("red")
            screen.draw.text("Time's Up! Your Final Score: " + str(score), midtop=(WIDTH/2,10),
            fontsize=40, color="white")        

def place_football():
      football.x = randint(70 , (WIDTH - 70))
      football.y = randint(70 , (HEIGHT - 70))

def time_up():
      global game_over
      game_over = True

def update():
      global score      

      if keyboard.left:
         footballer.x = footballer.x - 2
      if keyboard.right:
         footballer.x = footballer.x + 2      
      if keyboard.up:
          footballer.y = footballer.y - 2
      if keyboard.down:
          footballer.y = footballer.y + 2      

      football_collected = footballer.colliderect(football)

      if football_collected:    
         score = score + 10
         place_football()

clock.schedule(time_up, 60.0)
         
pgzrun.go()
