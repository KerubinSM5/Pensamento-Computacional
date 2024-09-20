import pygame
import time

# Constantes (normalmente escrevemos tudo em maiúsculo em Python)
LARGURA = 1000
ALTURA = 600
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (124, 124, 124)
POS_TEXTO_1 = (LARGURA / 2, 20)
POS_TEXTO_2 = (LARGURA / 2, 50)
POS_TEXTO_3 = (LARGURA / 2, 80)
POS_TEXTO_4 = (LARGURA / 2, 500)

# Variáveis
fim_linha = 100
passo = 1
cor_linha = VERDE

# Inicializa o Pygame
pygame.init()

# Define as dimensões e título da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Clicando e desenhando linhas")


def tela_inicial():
    # Preenche a tela de preto
    tela.fill(PRETO)
    # Escrever as opções do programa
    fonte = pygame.font.SysFont("Arial", 20)
    texto_1 = fonte.render("Opções: V - Verde / A - Azul / C - Cinza / L - Limpar", True, (255, 255, 255))
    texto_rect_1 = texto_1.get_rect(center=POS_TEXTO_1)
    tela.blit(texto_1, texto_rect_1)

    texto_2 = fonte.render("Opções: \u2191  \u2193 - Fim da linha / \u2190 \u2192 - Passo / R - Desenhar Linha", True,
                           (255, 255, 255))
    texto_rect_2 = texto_2.get_rect(center=POS_TEXTO_2)
    tela.blit(texto_2, texto_rect_2)
    if cor_linha == VERDE:
        cor = "Verde"
    elif cor_linha == AZUL:
        cor = "Azul"
    else:
        cor = "Cinza"
    texto_3 = fonte.render(f"Linha vai até coluna {fim_linha} com passo de {passo} com a cor {cor}", True,
                           (255, 255, 255))
    texto_rect_3 = texto_3.get_rect(center=POS_TEXTO_3)
    tela.blit(texto_3, texto_rect_3)
    pygame.display.flip()


def desenhar_linha():
    for coluna in range(1, fim_linha, passo):
        ponto = (coluna, 300)
        pygame.draw.circle(tela, cor_linha, ponto, 2)
        fonte = pygame.font.SysFont("Arial", 30)
        texto_4 = fonte.render(f"Coluna: {coluna}", True, cor_linha)
        texto_rect_4 = texto_4.get_rect(center=POS_TEXTO_4)
        tela.blit(texto_4, texto_rect_4)
        pygame.display.flip()
        time.sleep(0.3)
        pygame.draw.rect(tela, PRETO, texto_4.get_rect(center=POS_TEXTO_4))
        pygame.display.flip()
    time.sleep(1)


# Loop principal do jogo
tela_inicial()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                cor_linha = AZUL
            elif evento.key == pygame.K_c:
                cor_linha = CINZA
            elif evento.key == pygame.K_v:
                cor_linha = VERDE
            elif evento.key == pygame.K_LEFT:
                passo -= 1
                if passo < 1:
                    passo = 1
            elif evento.key == pygame.K_RIGHT:
                passo += 1
                if passo > 10:
                    passo = 10
            elif evento.key == pygame.K_UP:
                fim_linha += 1
                if fim_linha > 900:
                    fim_linha = 900
            elif evento.key == pygame.K_DOWN:
                fim_linha -= 1
                if fim_linha < 10:
                    fim_linha = 10
            elif evento.key == pygame.K_l:
                tela_inicial()
            elif evento.key == pygame.K_r:
                desenhar_linha()

            tela_inicial()

# Finaliza o Pygame
pygame.quit()
