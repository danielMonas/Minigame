# A mini-game using moving balls, based on physics and kinetic principles. August 2018
import pygame, sys, time, random
from PlayerClass import *
from EnemyClass import *

FPS = 30

def main():
    # Initializing Engine and font components
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    # Setting Screen
    size = width, height = SIZE, SIZE
    screen = pygame.display.set_mode(size)
    # Spawning the player and bots. Notice - The player spawns first
    player1 = Player((0,204,0), [])
    entities = [player1]
    for i in range(random.randint(2,10)):
        entities.append(Enemy(i, entities))
    clock = pygame.time.Clock()
    pygame.key.set_repeat(10,10)

    while 1:
        clock.tick(480)
        screen.fill((255,255,255))
        player1.catch_event()
        for e in entities[1:]:
            pygame.draw.circle(screen,e.color,e.location,e.radius)
            e.move_enemy(entities[1:])

        player1.check_collision(entities[1:])
        pygame.draw.circle(screen,player1.color,player1.location,player1.radius)

        pygame.display.update()
        clock.tick(FPS)
main()
