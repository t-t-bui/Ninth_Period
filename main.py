import pygame
from pygame.locals import *
import sys

# global variables
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 700
FPS = 60

# initialized game window
FRAMEPERSEC = pygame.time.Clock()
displaysurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# placeholder for character class
class Character(pygame.sprite.Sprite):
  # initialize character 
  def __init__(self):
    super().__init__()
    # self.image = pygame.image.load("images/Dino_Sprite/png/Character_Run.png")
    self.image = pygame.image.load("reDinoTWO.png")
    self.rect = self.image.get_rect() #makes the hitbox around the sprite image (I think??) 
    self.rect.center = (50, 330) #sets the position of the sprite
    self.isJump = False 

  def jump (self): 
    if keys[pygame.K_SPACE]: #if the spacebar is being pressed
      self.isJump = True #going to be used for gravity
      self.rect.y -= 50 #moves sprite up 50 pixels each time

  def gravity (self):
    if self.isJump == True:
      self.rect.y += 7.5 #enables sprite to fall back down/not stay in the air 

  # def draw (self, surface): #draws the sprite on the display
    # surface.blit(self.image, self.rect)  
    # self.image = pygame.image.load("images/Dino_Sprite/png/Character_Run.png")
    # self.image = pygame.image.load("reDinoTWO.png")
    # self.rect = self.image.get_rect()
    # self.rect.center = (10,400)
    
# background class
class background():
  #initialize background image
  def __init__(self):
    self.bgimage = pygame.image.load("images/pixel_landscape.png")
    self.rectBGpng = self.bgimage.get_rect()

    self.bgY1 = 0
    self.bgX1 = 0

    self.bgY2 = self.rectBGpng.height
    self.bgX2 = 0

    self.moving_speed = 0.5

  # TODO: fix update and render to have a smoother transition instead of translate image
  def update(self):
    # width, height = self.bgimage.get_size()
    # copydisplaysurface = self.bgimage.copy()
    # displaysurface.blit(copydisplaysurface, (0, 0), (width - self.moving_speed, 0, self.moving_speed, height))

    # get the x axis attribute and update it to move using the moving speed
    self.bgX1 -= self.moving_speed
    self.bgX2 -= self.moving_speed

    # checking window boundaries
    if self.bgX1 <= -self.rectBGpng.width:
      self.bgX1 = self.rectBGpng.width
    if self.bgX2 <= self.rectBGpng.width:
      self.bgX2 = self.rectBGpng.width

  def render(self):
    width, height = self.bgimage.get_size()
    # copydisplaysurface = self.bgimage.copy()
    # displaysurface.blit(copydisplaysurface, (0, 0), (width - self.moving_speed, 0, self.moving_speed, height))

    # update coordinate system (i.e x axis of the background image) to translate image 
    displaysurface.blit(self.bgimage, (self.bgX1, self.bgY1))
    displaysurface.blit(self.bgimage, (self.bgX2, self.bgY2))

def main():
  pygame.init()
  
  back_ground = background()
  dyno = Character()
  
  pygame.display.set_caption("DYNO GAME")

  all_sprites = pygame.sprite.Group()
  all_sprites.add(dyno)

  # game loop
  while True:
    #Cycles through all occurring events   
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    back_ground.update()
    back_ground.render()
    
    for sprite in all_sprites:
      displaysurface.blit(sprite.image, sprite.rect)
          
    pygame.display.update()
    FRAMEPERSEC.tick(FPS)

if __name__=="__main__":
  main()
