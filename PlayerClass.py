import pygame, random,sys
from BaseObject import *

DIMENSIONS = 2

class Player(Object):
    def __init__(self,col, entities):
        print("SPAWN PLAYER")
        Object.__init__(self, col, 25, [0,0], entities)


    def catch_event(self):
        """ Recognizing and handling keyboard input"""
        sprite = [0,0]
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            sprite = self.calculate_move(keys_pressed, sprite)
        self.update_movement(sprite)


    def calculate_move(self, keys_pressed, sprite):
        """ Calculating acceleration and speed according to keyboard input
            keys_pressed: a list of pressed keyboard keys
            sprite: a list of acceleration values for each dimension"""
        spritex, spritey = sprite
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            spritex -= 5
            self.velocity[0] -= 0.25
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            spritex += 5
            self.velocity[0] += 0.25
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            spritey -= 5
            self.velocity[1] -= 0.25
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            spritey += 5
            self.velocity[1] += 0.25
        return [spritex, spritey]


    def update_movement(self,sprite):
        """ Updating the player's location according to velocity and acceleration
            sprite: a list of acceleration values for each dimension"""
        new_loc = []
        for d in range(DIMENSIONS):
            if self.velocity[d] > 0:
                self.velocity[d] -= 0.05
            elif self.velocity[d] < 0:
                self.velocity[d] += 0.05

            new_loc.append(int(self.location[d] + 0.5 * (sprite[d]**2) + self.velocity[d]))
            if self.find_d_walls(new_loc[d]):
                sprite[d] *= -1
                self.velocity[d] *= -1
        self.move(sprite)


    def check_collision(self, enemyList):
        """ Checking if the player has passed through an enemy bot
            enemyList: a list of enemy object to compare against"""
        for enemy in enemyList:
            if self.collision(enemy):
                self.color = random.randint(5,250),random.randint(5,250),random.randint(5,250)
