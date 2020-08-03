import pygame,random
from variable import white, black, green, brown, sc_ancho, sc_largo,BalleSpeed, Nspeed, bax, bay, vidamuralla
from Imagenes import General, background1,Ballesta_anim, Nflecha, Fflecha, muro1,barra, LanceroAC, LanceroAE, murolvl1, Protector
from Controles import SubirUP, BajarDo, F_fuego, F_normal, Fnormal
pygame.init()

##--------------Clase en pruebas (costo computacional elevado; razon: desconocida)----------------
class imagenblock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def esta (self, sheet, x,y, colork, screen):
        self.image = pygame.image.load(sheet).convert()
        self.image.set_colorkey(colork)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, self. rect)

    def update():
        pass

#------------------------------------------------------------------------------------------------
##--------------Objetos inanimados de la pantalla------------------------------------------------
class Escudo(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.shield = vidamuralla
        self.image = pygame.image.load(murolvl1).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 145
     
    def update(self):
        pass 

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(background1).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        pass

class Barra1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(barra).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = bax
        self.rect.y = bay
    
    def update(self):
        pass

class Muro1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(muro1).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 642
    
    def update(self):
        pass

##--------------Objetos animados----------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load(Ballesta_anim)
        self.sheet.set_colorkey(white)
        self.sheet.set_clip(pygame.Rect(0,0,134,99))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.centerx = 78
        self.rect.bottom = sc_ancho //2
        self.frame = 0
        self.refill = {0: (0,0,134,99), 1: (141,0,134,99)}
        self.refill2 = {0: (0,99,134,99), 1: (141,99,134,99)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set)-1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'up':
            if self.rect.y < 120:
                pass
            else:
                self.rect.y -= BalleSpeed 

        if direction == 'down':
            if self.rect.y > 590:
                pass
            else:
                self.rect.y += BalleSpeed

        if direction == 'stop':
            self.rect.y += 0
    
        if direction == 'Fnormal D':
            self.clip(self.refill)
        
        if direction == 'Fnormal R':
            self.clip(self.refill[0])

        if direction == 'Ffire D':
            self.clip(self.refill2)
        
        if direction == 'Ffire R':
            self.clip(self.refill2[0])
        
        #if self.TipoF == "fire":
            #if direction == 'shot':
             #   self.clip(self.refill2)
            #if direction == 'recarga':
             #   self.clip(self.refill2[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event, normal, fuego):
        #Agregat otro if para disparar con el mouse
        if event.type == pygame.KEYDOWN:

            if event.key == SubirUP:
                self.update('up')
            if event.key == BajarDo:
                self.update('down') 

            if normal == True:
                if event.key == Fnormal:
                    self.update('Fnormal D')
            if fuego == True:
                if event.key == Fnormal:
                    self.update('Ffire D')

        if event.type == pygame.KEYUP:

            if event.key == SubirUP:
                self.update('stop')
            if event.key == BajarDo:
                self.update('stop') 
            if event.key == F_normal:
                self.update('Fnormal R')
            if event.key == F_fuego:
                self.update('Ffire R')
            if normal == True: 
                if event.key == Fnormal:
                    self.update('Fnormal R')
            if fuego == True:
                if event.key == Fnormal:
                    self.update('Ffire R')

    def Nshoot(self, bullets, all_sprites):
        bullet = NArrows(self.rect.right, self.rect.centery,Nflecha )
        all_sprites.add(bullet)
        bullets.add(bullet)

    def Fshoot(self, bullets, all_sprites):
        bullet = NArrows(self.rect.right, self.rect.centery, Fflecha)
        all_sprites.add(bullet)
        bullets.add(bullet)  

class General1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load(General)
        self.sheet.set_colorkey(white)
        self.sheet.set_clip(pygame.Rect(300,0,75,51))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.centerx = bax+ 150
        self.rect.bottom = bay + 70
        self.frame = 0
        self.Tdefend = (0,0,75,51)
        self.Thorses = (75,0,75,51)
        self.TfireAr = (150,0,75,51)
        self.Tnormal = (275,0,75,51)

    def update(self):
        pass

class NArrows(pygame.sprite.Sprite):
    def __init__(self,x,y,Pflecha):
        super().__init__()
        self.image = pygame.image.load(Pflecha)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.x = x
        self.speed = Nspeed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > sc_largo:
            self.kill()

class Lancero1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LanceroAC).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = sc_largo
        self.rect.y = random.randrange(135,590)
        self.speedx = random.randrange(-3,-1)
        self.speedy = random.randrange(-1,1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.y > 590 or self.rect.y <120:
            self.speedy = self.speedy * -1
        
        if self.rect.x < 104:
            self.speedx = -1
            self.rect.x = self.rect.x + 20

class Lancero2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load(LanceroAE)
        self.sheet.set_colorkey(white)
        self.sheet.set_clip(pygame.Rect(0,0,59,40))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = sc_largo
        self.rect.y = random.randrange(135,590)
        self.speedx = random.randrange(-3,-1)
        self.speedy = random.randrange(-1,1)
        self.sescudo = {0:(59,0,59,40)}
        self.life = 2

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.y > 590 or self.rect.y <120:
            self.speedy = self.speedy * -1
        
        if self.rect.x < 104:
            self.speedx = -1
            self.rect.x = self.rect.x + 20

##--------------Partes de la barra y poderes-----------------------------------------------------
class vida(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(Protector).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_shield_bar(self,surface, percen,color):  
        self.fill = (percen/100) * 83
        self.fill = pygame.Rect(self.rect.x,self.rect.y+5,70,self.fill)
        pygame.draw.rect(surface, color, self.fill)
        surface.blit(self.image, self.rect)

    def draw_text(self,surface, text, size):
        self.font = pygame.font.SysFont("serif", size)
        self.text_surface = self.font.render(text, True, white)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect = (self.rect.x, self.rect.y)
        surface.blit(self.text_surface, self.text_rect)




