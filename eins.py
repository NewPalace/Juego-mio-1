import pygame, random
from clases import Player, General1, Lancero1, Lancero2, vida
from clases import  Fondo, Muro1, Barra1, imagenblock, Escudo
from variable import white,skyblue, green, black,green, sc_ancho, sc_largo, ticK, Textbarup, bax, bay
from Imagenes import  Icono
from Controles import Disparo1

pygame.mixer.init()

def main():
    pygame.init()
    screen = pygame.display.set_mode([sc_largo, sc_ancho])
    clock = pygame.time.Clock()
    score = 0

    #Personalizacion de la ventana
    pygame.display.set_caption(Textbarup)
    icon = pygame.image.load(Icono)
    icon.set_colorkey(black)
    pygame.display.set_icon(icon)

    #Guardado de sprites
    all_sprites = pygame.sprite.Group()
    lancerolvl1 = pygame.sprite.Group()
    lancerolvl2 = pygame.sprite.Group()
    lancerolvl22 = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    #"inicializacion" de clases
    fondo = Fondo()
    general = General1()
    muro = Muro1()
    Play = Player()
    barra = Barra1()
    escudo = Escudo(screen)
    vida1 = vida(bax+162,bay)
    expe = vida(bax+285, bay)
    lazul = Lancero1()
    eazul = Lancero2()

    all_sprites.add(escudo)

    #generacion de enemigos (se pasara a una clase cuando se termine)
    for i in range(5):
        lazul = Lancero1()
        lancerolvl1.add(lazul)
        all_sprites.add(lazul)
    for i in range(1):
        eazul = Lancero2()
        lancerolvl2.add(eazul)
        all_sprites.add(eazul)
    #eazul1 = Lancero2()
    #eazul2 = Lancero2()
    #eazul3 = Lancero2()
    #eazul4 = Lancero2()

    #lancerolvl2.add(eazul1)
    #lancerolvl2.add(eazul2)
    #lancerolvl2.add(eazul3)
    #lancerolvl2.add(eazul4)

    #all_sprites.add(eazul1)
    #all_sprites.add(eazul2)
    #all_sprites.add(eazul3)
    #all_sprites.add(eazul4)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == Disparo1:
                    Play.Nshoot(bullets, all_sprites)

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
            score += 1

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
                done =True

        hits = pygame.sprite.spritecollide(escudo, lancerolvl2, False)
        for hit in hits:
            escudo.shield = escudo.shield - 5
            if escudo.shield <= 0:
                done =True
            
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
        #General
        screen.blit(general.image, general.rect)

        pygame.display.flip()

        clock.tick(ticK)

    pygame.quit()

if __name__ == "__main__":
	main() 
