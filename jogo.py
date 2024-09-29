import pygame 
from pygame.locals import *
from sys import exit
from random import randint 

pygame.init()
#cores = [(0, 255, 0),(255, 0, 0),(0, 0, 255),(255, 255, 0),(255, 165, 0),]
largura  = 640
altura = 480

x_cobra = largura/2
y_cobra = altura/2

velocidade = 10
x_controle = velocidade
y_controle = 0 

x_maca = randint(40, 600)
y_maca = randint(50,430)

fonte = pygame.font.Font('Minecraft.ttf', 40)
pontos=0
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.circle(tela,(0,255,0), (XeY[0], XeY[1]), 10)

def reiniciarjogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = randint(40, 600)
    y_cobra = randint(50,430)
    x_maca = randint(40, 600)
    y_maca = randint(50,430)    
    morreu = False


while True:
    relogio.tick(20)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    textoFormatado = fonte.render(mensagem, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle != velocidade:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle != -velocidade:
                    x_controle= velocidade
                    y_controle = 0

            if event.key == K_s:
                if y_controle != -velocidade:
                    y_controle = velocidade
                    x_controle = 0

            if event.key == K_w:
                if y_controle != velocidade:
                    y_controle = -velocidade
                    x_controle = 0
                
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    # Lógica de teletransporte: verificar se a cobra saiu da tela
    if x_cobra >= largura:  # Saiu pela direita
        x_cobra = 0
    if x_cobra < 0:  # Saiu pela esquerda
        x_cobra = largura
    if y_cobra >= altura:  # Saiu pelo fundo
        y_cobra = 0
    if y_cobra < 0:  # Saiu pelo topo
        y_cobra = altura

    cobra = pygame.draw.circle(tela, (255,0,255), (x_cobra, y_cobra), 10)
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 15, 15))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 1
    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.Font('Minecraft.ttf', 20)
        mensagem = 'Perdeu, tecle "q" para reiniciar'
        textoFormatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = textoFormatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        reiniciarjogo()

            ret_texto.center = (largura//2, altura//2 )
            tela.blit(textoFormatado, ret_texto)
            pygame.display.update()

    if len(lista_cobra) > comprimento_inicial+1:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)

    tela.blit(textoFormatado, (450, 40))
    pygame.display.update()