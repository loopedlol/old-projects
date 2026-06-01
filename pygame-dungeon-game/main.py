import pygame
from level import *
from player import *

pygame.init()
size = (height, width) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
images = {
  "w" : "images/tiles/floor13.gif",
  "f" : "images/tiles/roomWall13.gif",
  "player" : "images/player/superhero.gif",
  "closedDoor" : "images/tiles/door11.gif",
  "openedDoor" : "images/tiles/openDoor11.gif",
  "bat" : "images/monsters/bat.gif",
}

levelNumber = 0
levels = []

player = 0
level = 0

def process_events(player):
  global running

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        player.updateMoveDirection("w")
      elif event.key == pygame.K_s:
        player.updateMoveDirection("s")
      elif event.key == pygame.K_a:
        player.updateMoveDirection("a")
      elif event.key == pygame.K_d:
        player.updateMoveDirection("d")

def changeLevel(type):
  global level, player, levelNumber

  if type == "exitDoor":
    levelNumber += 1
    if len(levels) - 1 >= levelNumber:
      level = levels[levelNumber]
      player.mapLayout = level.mapLayout
      level.findEligibleSpawn(level.structurePositions["enterDoor"])
    else:
      level = RandomLevel(images, player)
      player.mapLayout = level.mapLayout
      levels.append(level)

  if type == "enterDoor" and levelNumber > 0:
    levelNumber -= 1
    level = levels[levelNumber]
    player.mapLayout = level.mapLayout
    level.findEligibleSpawn(level.structurePositions["exitDoor"])


def main():
  global running, level, player
  player = Player(images["player"], [0, 0])
  level = RandomLevel(images, player)
  player.mapLayout = level.mapLayout
  levels.append(level)
  
  while running:
    process_events(player)
    changeLevel(player.checkStructures(level.structurePositions))
  
    level.draw(screen)
    level.update()
  
    pygame.display.update()

    clock.tick(60)
  
  pygame.quit()

if __name__ == "__main__":
  main()
