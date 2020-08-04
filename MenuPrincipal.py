from ModoScore import ModoScore1
from variable import sc_ancho, sc_largo, bax, bay, ticK
from clases import vida
import pygame

def Menu():
    pygame.init()
    option = True
    screen = pygame.display.set_mode([sc_largo, sc_ancho])
    clock = pygame.time.Clock()
    if option:
        Texto_1 = vida(bax+40,sc_ancho//3)
        Texto_2 = vida(bax+60,sc_ancho//2)
        Texto_22 = vida(bax+60,sc_ancho//2+25)
        #Texto_3 = vida(bax+250,sc_ancho*2//3)
        Texto_1.draw_text(screen, "Defiende la muralla!!", 65)
        Texto_2.draw_text(screen, "Presiona el numero del modo que quieres jugar.", 25)
        Texto_22.draw_text(screen, "1.- Modo Score", 25)
        #Texto_3.draw_text(screen, "Press SPACE", 20)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(ticK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        waiting = False
                        ModoScore1(screen)