import pygame

class Monster(pygame.sprite.Sprite):
  
  def __init__(self, imagePath, imagePosition, type):
    super().__init__()

    self.imagePath = imagePath 
    self.image = pygame.image.load(imagePath)
    self.rect = self.image.get_rect()
    self.rect.topleft = imagePosition
    self.type = type
    self.moveMonsterTypes = {
      "bat" : self.moveBat,
    }

  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def moveMonster(self, targetPosition):
    self.moveMonsterTypes[self.type](targetPosition)
  
  def moveBat(self, targetPosition):
    deltaX = targetPosition[0] - self.rect.x
    deltaY = targetPosition[1] - self.rect.y

    if deltaX > 0:
      self.rect.x += 1
    elif deltaX < 0:
      self.rect.x -= 1

    if deltaY > 0:
      self.rect.y += 1
    elif deltaY < 0:
      self.rect.y -= 1