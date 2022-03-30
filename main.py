import pygame
from pygame.locals import *

# global variables
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 700
FPS = 60

FRAMEPERSEC = pygame.time.Clock()

bg = pygame.image.load("images/pixel_landscape.png")

class background():
  def __init__(self):
    self.bgimage = pygame.image.load("images/pixel_landscape.png")
    self.rectBGpng = self.bgimage.get_rect()

    self.bgY1 = 0
    self.bgX1 = 0

    self.bgY2 = self.rectBGpng.height
    self.bgX2 = 0

def main():
  pygame.init()

  displaysurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("DYNO GAME")

  displaysurface.blit(bg, (0,0))

  pygame.display.update()
  FRAMEPERSEC.tick(FPS)

if __name__=="__main__":
  main()