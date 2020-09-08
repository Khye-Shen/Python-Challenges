import math


class planet:



    def __init__(self, mass, radius):

        self.mass = mass
        self.radius = radius


    def escape_velocity(self):
        v = math.sqrt(((2 * (6.67**-11) * self.mass) / (self.radius)))

        return v



Earth = planet(5.972**24, 6371000)

print(Earth.escape_velocity())