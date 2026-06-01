import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, playerSpritePath, playerPosition):
    super().__init__()

    self.imagePath = playerSpritePath
    self.image = pygame.image.load(playerSpritePath)
    self.rect = self.image.get_rect()
    self.rect.topleft = playerPosition
    self.moveDirection = ""
    self.mapLayout = []

  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def getPosition(self):
    return [self.rect.x, self.rect.y]

  def teleportPlayer(self, positionX, positionY):
    self.rect.x = positionX
    self.rect.y = positionY
    
  def updateMoveDirection(self, direction):
    self.moveDirection = direction
    
  def updatePlayer(self):
    if self.moveDirection == "w":
      if self.mapLayout[int(self.rect.y / 32) - 1][int(self.rect.x / 32)] == "f":
        self.rect.y -= 32
      
    elif self.moveDirection == "a":
      if self.mapLayout[int(self.rect.y / 32)][int(self.rect.x / 32) - 1] == "f":
        self.rect.x -= 32
      
    elif self.moveDirection == "s":
      if self.mapLayout[int(self.rect.y / 32) + 1][int(self.rect.x / 32)] == "f":
        self.rect.y += 32
      
    elif self.moveDirection == "d":
      if self.mapLayout[int(self.rect.y / 32)][int(self.rect.x / 32) + 1] == "f":
        self.rect.x += 32
      
    self.moveDirection = ""

  def checkStructures(self, structurePositions):
    if self.rect.x == structurePositions["exitDoor"][0] and self.rect.y == structurePositions["exitDoor"][1]: #could do this in a dictionary check for loop (do later)
      return "exitDoor"
    elif self.rect.x == structurePositions["enterDoor"][0] and self.rect.y == structurePositions["enterDoor"][1]:
      return "enterDoor"
    return "none"