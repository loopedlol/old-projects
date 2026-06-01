import pygame
import math
import random
from tile import *
from player import *
from monster import *

class Level(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.walls = pygame.sprite.Group()
    self.floors = pygame.sprite.Group()
    self.player = ""
    self.monsters = []
    self.closedDoor = ""
    self.openedDoor = ""

  def draw(self, screen):
    self.walls.draw(screen)
    self.floors.draw(screen)
    self.closedDoor.draw(screen)
    self.openedDoor.draw(screen)
    self.player.draw(screen)
    for i in range(0, len(self.monsters)):
      self.monsters[i].draw(screen)

  def update(self):
    self.player.updatePlayer()
    for i in range(0, len(self.monsters)):
      self.monsters[i].moveMonster(self.player.getPosition())

class RandomLevel(Level):
  def __init__(self, images, player):
    super().__init__()
    self.player = player
    self.mapLayout = []
    self.structurePositions = {}
    self.generate_level(images)

  def findEligibleSpawn(self, structurePosition):
    x = int(structurePosition[0]/32)
    y = int(structurePosition[1]/32)
    if self.mapLayout[y + 1][x] == "f":
      self.player.teleportPlayer(structurePosition[0], structurePosition[1] + 32)
    elif self.mapLayout[y - 1][x] == "f":
      self.player.teleportPlayer(structurePosition[0], structurePosition[1] - 32)
    elif self.mapLayout[y][x + 1] == "f":
      self.player.teleportPlayer(structurePosition[0] + 32, structurePosition[1])
    elif self.mapLayout[y][x - 1] == "f":
      self.player.teleportPlayer(structurePosition[0] - 32, structurePosition[1])

  def generate_level(self, images):
    game_map = []
    screen_info = pygame.display.Info()

    for j in range(math.ceil(screen_info.current_h/32)):
      row_format = []
      
      for i in range(math.ceil(screen_info.current_w/32)):
        row_format.append("w")
        
      game_map.append(row_format)

    total_tiles = len(game_map) * len(game_map[0])
    number_floors = total_tiles/2
    
    tile = [len(game_map)//2, len(game_map[0])//2]
    count = 0

    while count < number_floors:
      while game_map[tile[0]][tile[1]] == "f":
        randomNumber = random.randint(1, 4)
        if randomNumber == 1: #UP
          if tile[0] > 1:
            tile[0] -= 1
        elif randomNumber == 2: #RIGHT
          if tile[1] < math.ceil(screen_info.current_w/32) - 2:
            tile[1] += 1
        elif randomNumber == 3: #DOWN
          if tile[0] < math.ceil(screen_info.current_h/32) - 2:
            tile[0] += 1
        elif randomNumber == 4: #LEFT
          if tile[1] > 1:
            tile[1] -= 1

      game_map[tile[0]][tile[1]] = "f"
      count += 1

    self.mapLayout = game_map

    numberFloorsCount = 0

    for i in range(len(game_map)):
      for j in range(len(game_map[0])):
        
        type = game_map[i][j]
        imagePosition = [j * 32, i * 32]
        
        if type == "w":
          self.walls.add(Tile(images[type], imagePosition))
        elif type == "f":
          
          numberFloorsCount += 1

          if numberFloorsCount == 1:
            self.closedDoor = Door(images["closedDoor"], imagePosition)
            self.structurePositions["enterDoor"] = imagePosition

            if game_map[i + 1][j] == "f":
              self.player.teleportPlayer(imagePosition[0], imagePosition[1] + 32)
            elif game_map[i - 1][j] == "f":
              self.player.teleportPlayer(imagePosition[0], imagePosition[1] - 32)
            elif game_map[i][j + 1] == "f":
              self.player.teleportPlayer(imagePosition[0] + 32, imagePosition[1])
            elif game_map[i][j - 1] == "f":
              self.player.teleportPlayer(imagePosition[0] - 32, imagePosition[1])
              
          elif numberFloorsCount == number_floors:
            self.openedDoor = Door(images["openedDoor"], imagePosition)
            self.structurePositions["exitDoor"] = imagePosition
          else:
            self.floors.add(Tile(images[type], imagePosition))

          if numberFloorsCount == number_floors//2: #temporary monster placement
            self.monsters.append(Monster(images["bat"], imagePosition, "bat"))
