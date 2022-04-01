class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("reDinoTWO.png") #loads in reDinoTWO.png for the sprite
    self.rect = self.image.get_rect() #makes the hitbox around the sprite image (I think??) 
    self.rect.center = (50, 230) #sets the position of the sprite
    self.isJump = False 
    
  def jump (self): #incomplete because I need to add gravity !!
    if keys[pygame.K_SPACE]: #if the spacebar is being pressed
      self.isJump = True #going to be used for gravity
      self.rect.y -= 50 #moves sprite up 33 pixels each time

  def gravity (self):
    if self.isJump == True:
      self.rect.y += 7.5 #enables sprite to fall back down/not stay in the air
    
  def draw (self, surface): #draws the sprite on the display
    surface.blit(self.image, self.rect)