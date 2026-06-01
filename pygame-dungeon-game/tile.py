import pygame

class Tile(pygame.sprite.Sprite):
  def __init__(self, imagePath, imagePosition):
    super().__init__()

    self.imagePath = imagePath 
    self.image = pygame.image.load(imagePath)
    self.rect = self.image.get_rect()
    self.rect.topleft = imagePosition

class Door(pygame.sprite.Sprite):
  def __init__(self, imagePath, imagePosition):
    super().__init__()

    self.imagePath = imagePath
    self.image = pygame.image.load(imagePath)
    self.rect = self.image.get_rect()
    self.rect.topleft = imagePosition

  def draw(self, screen):
    screen.blit(self.image, self.rect)