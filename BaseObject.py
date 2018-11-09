import math
import random
SIZE = 600
X,Y = 0,1


class Object():
    def __init__(self, col, radius, velocity, others):
        self.color = col
        self.radius = radius
        self.spawn(others)
        self.velocity = velocity
        self.mass = math.pi * (self.radius**2)


    def spawn(self, others):
        """ Algorithm responsible for safe spawning of all game entities - ensuring the spawn location will not
            cause the entity to be stuck in a wall or spawn too close to another entity
            others = a list of the other entities for comparison """
        self.location = [0,0]
        invalid_location = True
        while invalid_location:
            invalid_location = False
            if self.find_walls():
                self.location = [random.randint(self.radius * 2,SIZE - self.radius),random.randint(self.radius * 2, SIZE - self.radius)]
                invalid_location = True
            for o in others:
                if self.collision(o):
                    self.location = [random.randint(self.radius * 2,SIZE - self.radius),random.randint(self.radius * 2, SIZE - self.radius)]
                    invalid_location = True


    def move(self, acceleration=[0,0]):
        # X = x0 + v0t + 0.5at**2 WHERE t = 1s => X = x0 + v0 + 0.5a
        for dimension in range(len(self.location)):
            self.location[dimension] += int(self.velocity[dimension] + 0.5 * acceleration[dimension])


    def find_walls(self, precaution = 0):
        x,y = self.location
        return self.find_d_walls(x, precaution) or self.find_d_walls(y, precaution)


    def find_d_walls(self,d, precaution = 10):
        return d - self.radius <= precaution or d + self.radius >= SIZE - precaution


    def collision(self,other,precaution = 1):
        return (self.location[0] - other.location[0])**2 + (self.location[1] - other.location[1])**2 <= (self.radius + other.radius)**2 + precaution
