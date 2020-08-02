import pygame, random
from clases import Player, General1, Lancero1, Lancero2, vida
from clases import  Fondo, Muro1, Barra1, imagenblock, Escudo, Game_Over
from variable import white,skyblue, green, black,green, sc_ancho, sc_largo, ticK, Textbarup, bax, bay, Nfle, Lanlvl1, explanlv1
from variable import mflefir, mflenor
from Imagenes import  Icono
from Controles import Fnormal, Ffire

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
    Gameo = Game_Over(screen)

    #Personalizacion de la ventana
    pygame.display.set_caption(Textbarup)
    icon = pygame.image.load(Icono)
    icon.set_colorkey(black)
    pygame.display.set_icon(icon)
  
    game_over = True
    done = False

    while not done:
        if game_over:

            #Gameo.show_go_screen()
            Texto_1 = vida(bax+80,sc_ancho//3)
            Texto_2 = vida(bax+225,sc_ancho//2)
            Texto_3 = vida(bax+250,sc_ancho*2//3)
            Texto_1.draw_text(screen, "OE PERDISTE? xd", 65)
            Texto_2.draw_text(screen, "Na mentira, xd", 25)
            Texto_3.draw_text(screen, "Press SPACE", 20)
            pygame.display.flip()
            waiting = True
            while waiting:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            waiting = False
#----------------------------------------------------------------------------
            game_over = False
            #Guardado de sprites
            all_sprites = pygame.sprite.Group()
            lancerolvl1 = pygame.sprite.Group()
            lancerolvl2 = pygame.sprite.Group()
            lancerolvl22 = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            bullets2 = pygame.sprite.Group()

            all_sprites.add(escudo)
            score = 0
            Flechas = Nfle
 
            #generacion de enemigos (se pasara a una clase cuando se termine)
            #Lanceros
            for i in range(Lanlvl1):
                lazul = Lancero1()
                lancerolvl1.add(lazul)
                all_sprites.add(lazul)
            
            #Escuderos


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == Fnormal:
                    Play.Nshoot(bullets, all_sprites)
                    Flechas -= mflenor
                    if Flechas <= 0:
                        game_over = True
                if event.key == Ffire:
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

        ##Lancero 2
        if eazul.life == 2:
            hits1 = pygame.sprite.groupcollide(lancerolvl2, bullets, False, True)
                    #eazul.sheet.set_clip(pygame.Rect(Play.get_frame(eazul.sescudo)))
                    #eazul.image = eazul.sheet.subsurface(eazul.sheet.get_clip())
                    #eazul.life = eazul.life - 1
            for hit in hits1:
                hit.sheet.set_clip(pygame.Rect(Play.get_frame(eazul.sescudo)))
                hit.image = hit.sheet.subsurface(hit.sheet.get_clip())
                hit.life = 1
               
        if eazul.life == 1:                                           
            hits2 = pygame.sprite.groupcollide(lancerolvl2, bullets, True, True)
            #all_sprites.remove(e)
            for hit in hits2:
                eazul = Lancero2()
                lancerolvl2.add(eazul)
                all_sprites.add(eazul)
                score += 2

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
            
        Play.handle_event(event)


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
