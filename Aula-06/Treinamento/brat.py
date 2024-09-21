import pygame

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bem vindo ao Pygame")

# Cria uma fonte
fonte = pygame.font.SysFont("Arial", 72)
texto = fonte.render("brat", True, (0, 0, 0))

# Loop principal do jogo
rodando = True
while rodando:
   for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           rodando = False

   # A tela ficará com fundo preto
   tela.fill((137, 204, 4))

   # Calcula a posição central do texto
   texto_rect = texto.get_rect(center=(largura//2, altura//2))
   # Renderiza o texto na tela
   tela.blit(texto, texto_rect)

   # Atualiza a tela
   pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
