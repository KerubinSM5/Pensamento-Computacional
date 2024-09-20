import pygame
import time
import random

# Inicializa o Pygame
pygame.init()


# Define as dimensões da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))#gera a tela
pygame.display.set_caption("Bem vindo ao Pygame")#Título da tela

# Loop principal do jogo
rodando = True
red = 0
green = 128
blue = 255
while rodando:
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           rodando = False


   # A tela ficará com fundo preto
   tela.fill((0, 0, 0))

   # Cria uma fonte
   fonte = pygame.font.SysFont("Arial", 36)  # define uma fonte e seu tamanho
   texto = fonte.render("Olá, Pygame!", True, (red, green, blue))  # define o texto para ser mostrado na tela

   '''red += 1
   green += 1
   blue += 1
   if red >255:
       red = 0
   if green >255:
       green = 0
   if blue >255:
       blue = 0'''

   red = random.randint(0,255)
   green = random.randint(0,255)
   blue = random.randint(0,255)

   time.sleep(0.25)

   # Calcula a posição central do texto
   texto_rect = texto.get_rect(center=(largura//2, altura//2))
   # Renderiza o texto na tela
   tela.blit(texto, texto_rect)


   # Atualiza a tela
   pygame.display.flip()


# Finaliza o Pygame
pygame.quit()
