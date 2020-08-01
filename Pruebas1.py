import pygame,random
from variable import white, black,green, sc_ancho, sc_largo
from Imagenes import General, background1,Ballesta_anim
pygame.init()


image = pygame.image.load(Ballesta_anim)
image.set_colorkey(white)
image.set_clip(pygame.Rect(0,0,134,99))
image = self.image.subsurface(self.image.get_clip())
rect = self.image.get_rect()
rect.centerx = 70
rect.bottom = sc_ancho //2
frame = 0
speed_y = 0
refill = {0: (0,0,134,99), 1: (141,0,275,99)}