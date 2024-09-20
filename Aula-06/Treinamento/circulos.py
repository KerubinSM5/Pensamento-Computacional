import pygame

# Constantes (normalmente escrevemos tudo em maiúsculo em Python)
LARGURA = 800
ALTURA = 600
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (124, 124, 124)
POS_TEXTO = (LARGURA / 2, 30)

# Inicializa o Pygame
pygame.init()

# Define as dimensões e título da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Clicando e desenhando Círculos")


def tela_inicial():
    # Preenche a tela de preto
    tela.fill(PRETO)
    # Escrever as opções do programa
    fonte = pygame.font.SysFont("Arial", 20)
    texto = fonte.render("Opções: V - Verde / A - Azul / C - Cinza / L - Limpar", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=POS_TEXTO)
    tela.blit(texto, texto_rect)
    pygame.display.flip() #redesenha a tela


# Loop principal do jogo
cor_circulo = VERDE
tela_inicial()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.pos[1] > 80: #desenha apenas abaixo das instruções
            # Desenha o círculo imediatamente após o clique, desde que esteja da linha 100 em diante
            pygame.draw.circle(tela, cor_circulo, evento.pos, 20) #o que é usado para desenhar na tela, como um pincel; evento.pos: posição onde foi clicada
            pygame.display.flip()#atualiza a tela novamente, porem com o círculo

        if evento.type == pygame.KEYDOWN: #Lê as teclas
            if evento.key == pygame.K_a:
                cor_circulo = AZUL
            elif evento.key == pygame.K_c:
                cor_circulo = CINZA
            elif evento.key == pygame.K_v:
                cor_circulo = VERDE
            elif evento.key == pygame.K_l:
                tela_inicial()

# Finaliza o Pygame
pygame.quit()
