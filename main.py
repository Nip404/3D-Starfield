from engine import Starfield
import pygame

# SETTINGS
refresh_screen = True
effect = False
follow_mouse = False

s = [800,600]

pygame.init()
screen = pygame.display.set_mode(s,0,32)
clock = pygame.time.Clock()
pygame.display.set_caption("3D Starfield by NIP")

def bbe(mode,s):
    for i in getattr(s,"stars"):
        i.fov += 2 if mode else -2
    
    return mode if -500 <= i.fov <= 500 else not mode

def follow(s):
    for i in getattr(s,"stars"):
        i.centre = pygame.mouse.get_pos()

def main():
    sf = Starfield(2000,screen)
    mode = True

    while True:
        clock.tick(60)

        if refresh_screen:
            screen.fill((0,0,0))

        if bb_effect:
            mode = bbe(mode,sf)

        if follow_mouse:
            follow(sf)
        
        sf.events()
        sf.draw()
        sf.animate()

        pygame.display.flip()

if __name__ == "__main__":
    main()
