import pygame

pygame.init()

##Poderes:
#Disparar 
Fnormal = pygame.K_j
#Poder Normal
F_normal = pygame.K_1
#Poder Fuego
F_fuego = pygame.K_2

#subir:
SubirUP = pygame.K_w

#Bajar:
BajarDo = pygame.K_s

def MostrarContoles(screen):
    from MenuPrincipal import Menu
    from variable import sc_largo, sc_ancho, bax, Textbarup, black, ticK
    from clases import vida
    from Imagenes import Icono

    pygame.init()
    screen = pygame.display.set_mode([sc_largo, sc_ancho])
    clock = pygame.time.Clock()

    #Personalizacion de la ventana
    pygame.display.set_caption(Textbarup)
    icon = pygame.image.load(Icono)
    icon.set_colorkey(black)
    pygame.display.set_icon(icon)


    Texto_1 = vida(bax+100,sc_ancho//3)
    Texto_2 = vida(bax+60,sc_ancho//2)
    Texto_22 = vida(bax+60,sc_ancho//2+25)
    Texto_3 = vida(bax+250,sc_ancho*2//3)
    Texto_31 = vida(bax+60,sc_ancho//2+50)
    Texto_32 = vida(bax+60, sc_ancho//2+75)
    Texto_1.draw_text(screen, "Controles", 65)
    Texto_2.draw_text(screen, "- (w) Subir", 25)
    Texto_22.draw_text(screen, "- (s) Bajar", 25)
    Texto_31.draw_text(screen, "- (j) Disparar",25)
    Texto_32.draw_text(screen, "- (1 y 2) Poderes (normal y fuego)", 25)
    Texto_3.draw_text(screen, "back(SPACE)", 20)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(ticK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    Menu()