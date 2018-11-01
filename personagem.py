import pygame

class Personagem(pygame.sprite.Sprite):
    listaImgs = []

    def __init__(self, lista):
        for img in lista:
            self.imagem = img
            self.rect = self.imagem.get_rect()
            self.rect.left, self.rect.top = 0, 240
            self.listaImgs.append([self.imagem, self.rect])
        


    def atualizar(self, tela, cont):
        tela.blit(self.listaImgs[cont][0], self.listaImgs[cont][1])

    def mover(self, x, y,cont):
        if(self.listaImgs[cont][1].left <= 950):
            self.listaImgs[cont][1].move_ip(x, y)

    def pular(self,cont):
        for img in self.listaImgs:
            img[1].move_ip(0,-200)
            #self.rect.move_ip(0, -150)

    def voltarPulo(self,cont):
        for img in self.listaImgs:
            img[1].top=240
        #self.rect.top = 240