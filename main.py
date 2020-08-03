import pygame, random
from clases import Player, General1, Lancero1, Lancero2, vida
from clases import  Fondo, Muro1, Barra1, imagenblock, Escudo
from variable import white,skyblue, green, black,green, sc_ancho, sc_largo, ticK, Textbarup, bax, bay, Nfle, Lanlvl1, explanlv1
from variable import mflefir, mflenor, vidamuralla
from Imagenes import  Icono
from Controles import Fnormal, F_fuego, F_normal

pygame.init()
pygame.mixer.init()

def main():
    pygame.init()
    screen = pygame.display.set_mode([sc_largo, sc_ancho])
    clock = pygame.time.Clock()

    #"inicializacion" de clases
    fondo = Fondo()
    general = General1()
    muro = Muro1()
    Play = Player()
    barra = Barra1()
    escudo = Escudo(screen)
    vida1 = vida(bax+163,bay)
    expe = vida(bax+285, bay)
    lazul = Lancero1()
    eazul = Lancero2()
    NumeroDeFlechas = vida(bax+38,bay+25)

    #Personalizacion de la ventana
    pygame.display.set_caption(Textbarup)
    icon = pygame.image.load(Icono)
    icon.set_colorkey(black)
    pygame.display.set_icon(icon)
    
    Normal = True
    Fuego = False
    game_over = True
    Win = False
    done = False
    Primeravez = 0
    while not done:
        #------------------------------------------------------------------Gameovers
        if game_over:
            if Primeravez == 0:
                Texto_1 = vida(bax+40,sc_ancho//3)
                Texto_2 = vida(bax+60,sc_ancho//2)
                Texto_22 = vida(bax+60,sc_ancho//2+25)
                Texto_3 = vida(bax+250,sc_ancho*2//3)
                Texto_1.draw_text(screen, "Defiende la muralla!!", 65)
                Texto_2.draw_text(screen, "- Pierdes si se te acaban las flechas o te quedas sin vida", 25)
                Texto_22.draw_text(screen, "- Ganas si completas el cuadro celeste (score)", 25)
                Texto_3.draw_text(screen, "Press SPACE", 20)
                pygame.display.flip()
                waiting = True
                escudo.shield = vidamuralla
                while waiting:
                    clock.tick(ticK)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_SPACE:
                                waiting = False
            
            if Primeravez > 0 :
                Texto_1 = vida(bax+60,sc_ancho//3)
                Texto_2 = vida(bax+180,sc_ancho//2)
                Texto_3 = vida(bax+250,sc_ancho*2//3)
                Texto_1.draw_text(screen, "OE PERDISTE? xd", 65)
                Texto_2.draw_text(screen, "Na mentira, intenta de nuevo!", 25)
                Texto_3.draw_text(screen, "Press SPACE", 20)
                pygame.display.flip()
                waiting = True
                escudo.shield = vidamuralla
                while waiting:
                    clock.tick(ticK)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_SPACE:
                                waiting = False
            Primeravez = Primeravez + 1
            game_over = False

            #Guardado de sprites
            all_sprites = pygame.sprite.Group()
            lancerolvl1 = pygame.sprite.Group()
            lancerolvl2 = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            bullets2 = pygame.sprite.Group()

            all_sprites.add(escudo)
            score = 0
            Flechas = Nfle
 
            #generacion de enemigos (se pasara a una clase cuando se termine)
            #Lanceros 1
            for i in range(Lanlvl1):
                lazul = Lancero1()
                lancerolvl1.add(lazul)
                all_sprites.add(lazul)
            
            #Lanceros 2
            #Aca iria el loop que generaria los lanceros

        if Win == True:
            Texto_1 = vida(bax+60,sc_ancho//3)
            Texto_2 = vida(bax+120,sc_ancho//2)
            Texto_22 = vida(bax+120,sc_ancho//2+25)
            Texto_3 = vida(bax+250,sc_ancho*2//3)
            Texto_1.draw_text(screen, "Ganaste agilado!", 65)
            Texto_2.draw_text(screen, "- LLegas a otra partidita", 25)
            Texto_22.draw_text(screen, "- O te achicas?", 25)
            Texto_3.draw_text(screen, "Press SPACE", 20)
            pygame.display.flip()
            waiting = True
            escudo.shield = vidamuralla
            while waiting:
                clock.tick(ticK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            waiting = False
        
            Primeravez = Primeravez + 1
            Win = False

            #Guardado de sprites
            all_sprites = pygame.sprite.Group()
            lancerolvl1 = pygame.sprite.Group()
            lancerolvl2 = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            bullets2 = pygame.sprite.Group()

            all_sprites.add(escudo)
            score = 0
            Flechas = Nfle
 
            #generacion de enemigos (se pasara a una clase cuando se termine)
            #Lanceros 1
            for i in range(Lanlvl1):
                lazul = Lancero1()
                lancerolvl1.add(lazul)
                all_sprites.add(lazul)
            
            #Lanceros 2
            #Aca iria el loop que generaria los lanceros


        #----------------------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == F_normal:
                    Normal = True
                    Fuego = False
                if event.key == F_fuego:
                    Normal = False
                    Fuego = True

                if Normal == True:
                    if event.key == Fnormal:
                        Play.Nshoot(bullets, all_sprites)
                        Flechas -= mflenor
                        if Flechas <= 0:
                            game_over = True
                if Fuego == True:
                    if event.key == Fnormal:
                        Play.Fshoot(bullets2,all_sprites)
                        Flechas -= mflefir
                        if Flechas <= 0:
                            game_over = True
        #Imagen de fondo  
        screen.blit(fondo.image, fondo.rect)
        all_sprites.draw(screen)

        #Colisones de flechas
        ##Lancero 1
        hits = pygame.sprite.groupcollide(lancerolvl1, bullets, True, True)
        for hit in hits:
            lazul = Lancero1()
            lancerolvl1.add(lazul)
            all_sprites.add(lazul)
            score += explanlv1

        hits3 = pygame.sprite.groupcollide(lancerolvl1, bullets2, True, True)
        for hit in hits3:
            lazul = Lancero1()
            lancerolvl1.add(lazul)
            all_sprites.add(lazul)
            score += explanlv1

        if score == 100:
            Win = True

        ##Lancero 2
        #Aca iria el codigo que reconoce la colicion de el lancero con escudo y la flecha

        #Barra de vida
        hits = pygame.sprite.spritecollide(escudo, lancerolvl1, False)
        for hit in hits:
            escudo.shield = escudo.shield - 3
            if escudo.shield <= 0:
                game_over =True

        hits = pygame.sprite.spritecollide(escudo, lancerolvl2, False)
        for hit in hits:
            escudo.shield = escudo.shield - 5
            if escudo.shield <= 0:
                game_over =True
            
        all_sprites.update()


        Play.handle_event(event,Normal,Fuego)


        #Escudo de la muralla
        screen.blit(escudo.image, escudo.rect)

        #Ballesta
        screen.blit(Play.image, Play.rect)

        #muro de abajo
        screen.blit(muro.image, muro.rect)

        #Barra de movimientos
        screen.blit(barra.image, barra.rect)
        vida1.draw_shield_bar(screen, escudo.shield, green)
        expe.draw_shield_bar(screen,score,skyblue)
        NumeroDeFlechas.draw_text(screen, str(Flechas), 15)

        #General
        screen.blit(general.image, general.rect)

        pygame.display.flip()

        clock.tick(ticK)

    pygame.quit()

if __name__ == "__main__":
	main() 
