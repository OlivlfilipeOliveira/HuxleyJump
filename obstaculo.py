import pygame


class Obstaculo(pygame.sprite.Sprite):

    def __init__(self, imagem,t=330):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.left, self.rect.top = 1037, t

    def atualizar(self, tela):
        tela.blit(self.imagem, self.rect)

    def mover(self, x, y):
        self.rect.move_ip(x, y)

    def verificacao(self):
        if(self.rect.left < -10):
            self.rect.left = 1037

    def getLeft(self):
        return self.rect.left
