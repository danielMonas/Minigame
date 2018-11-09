import random
from BaseObject import *
import math

class Enemy(Object):
    def __init__(self, id, others):
        print("SPAWN ENEMY")
        Object.__init__(self,(0, 0 + id * 10, 0 + id * 20), random.randint(5,51), [random.randint(-6,6),random.randint(-6,6)], others)
        self.id = id


    def move_enemy(self,others):
        """ Moving the enemy bot by calculating the effects of the bot's surroundings
            others = a list of all of the game's bots """
        if self.find_d_walls(self.location[X],5):
            self.velocity[X] *= -1
        if self.find_d_walls(self.location[Y],5):
            self.velocity[Y] *= -1
        for o in others:
            if self.collision(o) and self.id != o.id:
                self.knockback(o)
        self.move()


    def knockback(self, other):
        print("Debug for bot id {0} WITH bot id {1}:".format(self.id, other.id))
        dx = abs(self.location[0] - other.location[0])
        dy = abs(self.location[1] - other.location[1])
        print("dx = {0}, dy = {1}".format(dx,dy))
        theta = math.atan2(dy,dx)
        print("theta = {0}".format(math.degrees(theta)))
        print("OLD Vx = {0}, Vy = {1}".format(self.velocity[X], self.velocity[Y]))
        v0 = math.sqrt(self.velocity[X]**2 + self.velocity[Y]**2)
        sign = lambda x: (1, -1)[x < 0]
        self.velocity[X] = v0 * math.cos(theta) * -1 * sign(self.velocity[X])
        self.velocity[Y] = v0 * math.sin(theta) * -1 * sign(self.velocity[Y])
        print("NEW Vx = {0}, Vy = {1}".format(self.velocity[X], self.velocity[Y]))
        self.move([1,1])
