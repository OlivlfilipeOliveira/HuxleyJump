import pygame
import os
import random

from personagem import Personagem
from obstaculo import Obstaculo


def colisao(rec1, rec2):
    if(rec1.rect.colliderect(rec2)):
        return True
    return False

def calculaVelocidade(pontuacao, xbola):
    if(pontuacao % 30 == 0):
        xbola += 0.002
    return xbola


def menu():
    pygame.init()
    tela = pygame.display.set_mode((1036, 517))
    pygame.display.set_caption("HuxleyJump")

    icone = pygame.image.load(os.path.join("imgs/icone.jpg")).convert_alpha()
    pygame.display.set_icon(icone)

    background = pygame.image.load(os.path.join("imgs/fundo.png")).convert()
    textoHuxleyJump = pygame.image.load(
        os.path.join("imgs/textoHJ.png")).convert_alpha()
    botaoIniciar = pygame.image.load(os.path.join(
        "imgs/botoes/iniciar.png")).convert_alpha()
    botaoTutorial = pygame.image.load(os.path.join(
        "imgs/botoes/tutorial.png")).convert_alpha()
    botaoSobre = pygame.image.load(os.path.join(
        "imgs/botoes/sobre.png")).convert_alpha()

    retIniciar = botaoIniciar.get_rect()
    retIniciar.left, retIniciar.top = 450, 300

    retTutorial = botaoTutorial.get_rect()
    retTutorial.left, retTutorial.top = 450, 370

    retSobre = botaoSobre.get_rect()
    retSobre.left, retSobre.top = 450, 440
    #retIniciar.left,retIniciar.top=botaoIniciar.left,botaoIniciar.top
    sair = False

    while not sair:

        tela.blit(background, (0, 0))

        tela.blit(textoHuxleyJump, (270, 20))
        tela.blit(botaoIniciar, retIniciar)
        tela.blit(botaoTutorial, retTutorial)
        tela.blit(botaoSobre, retSobre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if(retIniciar.collidepoint(x, y)):
                    main()

                if(retSobre.collidepoint(x, y)):
                    sobre()

                if(retTutorial.collidepoint(x, y)):
                    tutorial()

        pygame.display.update()

    pygame.quit()


def main():
    pygame.init()

    #Variaveis
    bgX = 0
    veloc = 0
    branco = (255, 255, 255)
    vermelho = (255, 0, 0)
    contador = 0
    pontuacao = 0
    xbola = 1
    contSprite = 0
    sair = False
    colidiu = False

    tela = pygame.display.set_mode((1036, 517))
    pygame.display.set_caption("HuxleyJump")

    icone = pygame.image.load(os.path.join("imgs/icone.jpg")).convert_alpha()
    pygame.display.set_icon(icone)

    background = pygame.image.load(os.path.join("imgs/fundo.png")).convert()
    tela.blit(background, (0, 0))

    ender = "imgs/sprites/"
    sp1 = pygame.image.load(os.path.join(ender+"1.png")).convert_alpha()
    sp2 = pygame.image.load(os.path.join(ender+"2.png")).convert_alpha()
    sp3 = pygame.image.load(os.path.join(ender+"3.png")).convert_alpha()
    sp4 = pygame.image.load(os.path.join(ender+"4.png")).convert_alpha()
    sp5 = pygame.image.load(os.path.join(ender+"5.png")).convert_alpha()
    sp6 = pygame.image.load(os.path.join(ender+"6.png")).convert_alpha()
    sp7 = pygame.image.load(os.path.join(ender+"7.png")).convert_alpha()
    sp8 = pygame.image.load(os.path.join(ender+"8.png")).convert_alpha()
    sp9 = pygame.image.load(os.path.join(ender+"9.png")).convert_alpha()
    sp10 = pygame.image.load(os.path.join(ender+"10.png")).convert_alpha()

    lista = [sp1, sp2, sp3, sp4, sp5, sp6, sp7, sp8, sp9, sp10]

    jogador = Personagem(lista)

    obst = pygame.image.load(os.path.join(
        "imgs/obstaculo.png")).convert_alpha()
    bola = Obstaculo(obst)
    bola2 = Obstaculo(obst,60)

    bolas = [bola, bola2]

    botaoVoltar = pygame.image.load(os.path.join(
        "imgs/botoes/voltar.png")).convert_alpha()
    retVoltar = botaoVoltar.get_rect()
    retVoltar.left, retVoltar.top = 450, 400

    musica = pygame.mixer.music.load(os.path.join(
        "musica", "crazy.mp3"))  # Carrega a musica
    musica = pygame.mixer.music.play(-1)  # Toca a musica infinitamente (-1)

    pulo = pygame.mixer.Sound(os.path.join("musica/pulo.ogg"))

    fonte = os.path.join("fonte", "RAVIE.ttf")
    pontuacaoTexto = pygame.font.Font(fonte, 32)

    relogio=pygame.time.Clock()

    while not sair:
        
        if not colidiu:
            #Linhas que fazem com que o background se movimente.
            # o resto da divisao do x do background pela largura da tela
            relX = bgX % background.get_rect().width
            tela.blit(background, (relX - background.get_rect().width, 0))
            if(relX < 1036):
                tela.blit(background, (relX, 0))
            bgX -= 1

            jogador.atualizar(tela,contSprite)
            
            if(bola.getLeft() <= -10):
                indice = random.randint(0, 1)
                bola = bolas[indice]

            bola.atualizar(tela)

            textoPontos = pontuacaoTexto.render(
                "Pontuação: %d" % pontuacao, True, branco)

            xbola = calculaVelocidade(pontuacao, xbola)
            bola.mover(-xbola, 0)

            bola.verificacao()

            jogador.mover(veloc, 0,contSprite)

            tela.blit(textoPontos, (700, 20))

            contador += 1
            
            if(contador == 60): #pontuacao
                pontuacao += 1
                contador = 0

            if(contador%30==0): #movimento do boneco
                contSprite += 1

            if(contSprite>=10): #quantidade de imagens de sprite
                contSprite=0

        else:
            # Sobrepoe os elementos pra fazer com que eles desapareçem
            tela.blit(background, (0, 0))
            perdeu = pontuacaoTexto.render(
                "Você perdeu!", True, (255, 255, 255))
            recomecar = pontuacaoTexto.render(
                "Clique com o botão esquerdo pra recomeçar.", False, branco)
            textoPontos = pontuacaoTexto.render(
                "Pontuação: %d" % pontuacao, True, vermelho)

            tela.blit(perdeu, (370, 150))
            tela.blit(textoPontos, (370, 200))
            tela.blit(recomecar, (50, 250))
            tela.blit(botaoVoltar, retVoltar)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    veloc += 1

                if event.key == pygame.K_SPACE:
                    pulo.play()
                    jogador.pular(contSprite)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jogador.voltarPulo(contSprite)
                if event.key == pygame.K_RIGHT:
                    veloc = 0

            if (event.type == pygame.MOUSEBUTTONDOWN and colidiu == True):
                x, y = pygame.mouse.get_pos()
                if(retVoltar.collidepoint(x, y)):
                    pygame.mixer.music.stop()
                    menu()
                else:
                    colidiu == False
                    main()

        if(colisao(jogador, bola)):
            colidiu = True

        relogio.tick(1000)
        pygame.display.update()

    pygame.quit()


def tutorial():
    pygame.init()
    tela = pygame.display.set_mode((1036, 517))
    pygame.display.set_caption("HuxleyJump")

    icone = pygame.image.load(os.path.join("imgs/icone.jpg")).convert_alpha()
    pygame.display.set_icon(icone)

    relogio = pygame.time.Clock()

    #VARs
    cont1 = 0
    cont2 = 0
    prox = False

    background = pygame.image.load(os.path.join("imgs/fundo.png")).convert()

    #IMGS
    img1 = pygame.image.load(os.path.join(
        "imgs/sprites/1.png")).convert_alpha()
    retImg1 = img1.get_rect()
    retImg1.left, retImg1.top = 50, 400

    img2 = pygame.image.load(os.path.join(
        "imgs/sprites/2.png")).convert_alpha()
    img3 = pygame.image.load(os.path.join(
        "imgs/sprites/3.png")).convert_alpha()
    lista = [img1, img2, img3]

    imagem = lista[0]

    texto1 = pygame.image.load(os.path.join(
        "imgs/mensagens/textoTutorialMover.png")).convert_alpha()
    texto2 = pygame.image.load("imgs/mensagens/atalho.png").convert_alpha()

    #BOTOES
    voltar = pygame.image.load(os.path.join(
        "imgs/botoes/voltar.png")).convert_alpha()
    retVoltar = voltar.get_rect()
    retVoltar.left, retVoltar.top = 500, 300

    proximo = pygame.image.load(os.path.join(
        "imgs/botoes/proximo.png")).convert_alpha()
    retProximo = proximo.get_rect()
    retProximo.left, retProximo.top = 650, 300

    sair = False

    while not sair:
        tela.blit(background, (0, 0))

        #EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if(retProximo.collidepoint(x, y)):
                    prox = True

                if(retVoltar.collidepoint(x, y)):
                    menu()

        if(cont1 >= 3):  # contador para mostrar os sprites da img andando
            cont1 = 0

        if(prox):  # se a pessoa clicar no botao prox vai pra "outra tela"
            tela.blit(background, (0, 0))
            if(cont2 < 3):  # contador p/ mostrar a img pulando
                retImg1.move_ip(0, -200)
                cont2 += 1
            else:
                retImg1.move_ip(0, 200)
                cont2 = 0

            tela.blit(background, (0, 0))

            tela.blit(img1, retImg1)
            tela.blit(texto2, (400, 150))
            retVoltar.left = 570
            tela.blit(voltar, retVoltar)

            cont2 += 1

        else:
            imagem = lista[cont1]
            retImagem = imagem.get_rect()
            retImagem.left, retImagem.top = (50, 130)

            tela.blit(imagem, retImagem)
            tela.blit(texto1, (400, 150))
            tela.blit(voltar, retVoltar)
            tela.blit(proximo, retProximo)

        cont1 += 1
        relogio.tick(5)
        pygame.display.update()

    pygame.quit()


def sobre():
    pygame.init()
    tela = pygame.display.set_mode((1036, 517))
    pygame.display.set_caption("HuxleyJump")

    icone = pygame.image.load(os.path.join("imgs/icone.jpg")).convert_alpha()
    pygame.display.set_icon(icone)

    background = pygame.image.load(os.path.join("imgs/fundo.png")).convert()

    texto = pygame.image.load(os.path.join(
        "imgs/mensagens/sobreTexto.png")).convert_alpha()
    botao = pygame.image.load(os.path.join(
        "imgs/botoes/voltar.png")).convert_alpha()
    retVoltar = botao.get_rect()
    retVoltar.left, retVoltar.top = 450, 400

    sair = False

    while not sair:
        tela.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if(retVoltar.collidepoint(x, y)):
                    menu()

        tela.blit(texto, (250, 50))
        tela.blit(botao, retVoltar)

        pygame.display.update()

    pygame.quit()


menu()
