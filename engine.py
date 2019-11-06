import pygame
import random
import sys

class Star:
    def __init__(self, x, y, z, surf, speed):
        self.ranges = [x, y, z]

        self.factorz = 128
        
        self.pos = self.get_pos(x, y, z)
        self.surf = surf
        self.speed = speed
        self.centre = [i/2 for i in [self.surf.get_width(), self.surf.get_height()]]

    def get_pos(self, x, y, z):
        return {"x": random.randrange(-x/2, x/2), "y": random.randrange(-y/2, y/2), "z": random.randrange(1, z)}

    def draw(self):
        try:
            pygame.draw.circle(self.surf, [(1 - self.pos["z"]/self.ranges[2])*255] * 3, list(map(int, (self.pos["x"]*(self.factor/self.pos["z"]) + self.centre[0], self.pos["y"]*(self.factor/self.pos["z"]) + self.centre[1]))), int((1 - self.pos["z"]/self.ranges[2])*2.5), 0)
        except:
            pass
        
    def animate(self):
        self.pos["z"] -= self.speed
        self.pos = self.get_pos(self.ranges[0], self.ranges[1], self.ranges[2]) if self.pos["z"] <= 0 or not all(0 <= i <= [self.surf.get_width(), self.surf.get_height()][p] for p, i in enumerate((self.pos["x"]*(self.factor/self.pos["z"]) + self.centre[0], self.pos["y"]*(self.factor/self.pos["z"]) + self.centre[1]))) else self.pos
        
class Starfield:
    def __init__(self, amount, surf, xrange=100, yrange=100, zrange=100, speedrange=1):
        self.stars = [Star(xrange, yrange, zrange, surf, random.randrange(4 - speedrange, 4 + speedrange)/5) for _ in range(amount)]

    def draw(self):
        for star in self.stars:
            star.draw()

    def animate(self):
        for star in self.stars:
            star.animate()

    def events(self, **custom):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            else:
                for e in custom.keys():
                    if e == event.type:
                        try:
                            custom[e]()
                        except Exception as err:
                            print("Error: %s" % err)
