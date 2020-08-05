import pygame, random
from clases import Player, General1, Lancero1, Lancero2, vida
from clases import  Fondo, Muro1, Barra1, imagenblock, Escudo
from variable import white,skyblue, green, black,green, sc_ancho, sc_largo, ticK, Textbarup, bax, bay, Nfle, Lanlvl1, explanlv1
from variable import mflefir, mflenor, vidamuralla
from Imagenes import  Icono
from Controles import Fnormal, F_fuego, F_normal

def ModoScore1(screen):
    from MenuPrincipal import Menu
    from variable import BalleSpeed
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
    tiempo = vida(60, 3)
    TextoTiempo = vida(5, 3)
    NumeroDeFlechas = vida(bax+38,bay+25)
    TextoScore = vida(bax+300, bay+30)
    NumeroScore = vida(bax+303, bay+50)

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
                Texto_1 = vida(bax+150,sc_ancho//3)
                Texto_2 = vida(bax+60,sc_ancho//2)
                Texto_22 = vida(bax+60,sc_ancho//2+25)
                Texto_3 = vida(bax+200,sc_ancho*2//3)
                Texto_1.draw_text(screen, "Modo Score", 65)
                Texto_2.draw_text(screen, "- Pierdes si se te acaban las flechas o te quedas sin vida", 25)
                Texto_22.draw_text(screen, "- Ganas si completas el cuadro celeste (score)", 25)
                Texto_3.draw_text(screen, "Start(SPACE)      Back(b)", 20)
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
                                Time = 0
                                Time = pygame.time.get_ticks()
                            
                            if event.key == pygame.K_b:
                                waiting = False
                                Menu()

                                
            
            if Primeravez > 0 :
                Texto_1 = vida(bax+100,sc_ancho//3)
                Texto_2 = vida(bax+180,sc_ancho//2)
                Texto_3 = vida(bax+200,sc_ancho*2//3)
                Texto_1.draw_text(screen, "Defeated", 65)
                Texto_2.draw_text(screen, "Let's try again! or try another mode...", 25)
                Texto_3.draw_text(screen, "Again(SPACE)     Menu(m)", 20)
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
                                Time = 0
                                Time = pygame.time.get_ticks()
                            
                            if event.key == pygame.K_m:
                                waiting = False
                                Menu()
                                
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
            #Time = 0
            
            

        if Win == True:
            Texto_1 = vida(bax+190,sc_ancho//3)
            Texto_2 = vida(bax+340,sc_ancho//2)
            texto_22 = vida(bax+ 240, sc_ancho//2)
            Texto_3 = vida(bax+130,sc_ancho//2+25)
            Texto_4 = vida(bax+200,sc_ancho*2//3)
            Texto_1.draw_text(screen, "Ganaste!", 65)
            texto_22.draw_text(screen, "Tiempo: ", 25)
            Texto_2.draw_text(screen, str(round((Time2 - Time)/1000)), 25)
            Texto_3.draw_text(screen, "Buen tiempo loco, lo podras mejorar?", 25)
            Texto_4.draw_text(screen, "Again(SPACE)     Menu(m)", 20)
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
                            Time = 0
                            Time = pygame.time.get_ticks()
                        if event.key == pygame.K_m:
                            waiting = False
                            Menu()
        
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

            #Time = 0
            #Time = pygame.time.get_ticks()
            #tiempo.draw_text(screen, Time, 34 )

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


        Play.handle_event(event,Normal,Fuego, BalleSpeed)


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
        TextoScore.draw_text2(screen, "Score", 15)
        NumeroScore.draw_text2(screen, str(score), 15)

        #General
        screen.blit(general.image, general.rect)

        #Reloj
        
        Time2 = pygame.time.get_ticks()
        
        TextoTiempo.draw_text(screen, "Time: ", 15)
        tiempo.draw_text(screen, str(round((Time2 - Time)/1000)),  15)

        pygame.display.flip()

        clock.tick(ticK)

    pygame.quit()