import random

def numeros():
   lista = []
   numeros = 0
   continuar = True
   while continuar:
       aleatorio = random.randrange(1, 60) #gera numeros aleatórios
       if aleatorio not in lista: #verifica se um numero sorteado pertence ou não à lista; #Not in: não permite repetição de numero numa sequencia (linha)
           lista.append(aleatorio)
           numeros += 1
           if numeros == 6:
               continuar = False
   return lista

def principal():
   jogos = int(input("Quer quantos jogos da megasena? "))
   arqSena = open('megasena.txt', 'w')
   for rep in range(jogos): #gera quantos jogos foram solicitados
       jogo = numeros()
       for num in jogo:
           arqSena.write(str(num).zfill(2) + ' ') #separador para os numeros
       arqSena.write('\r')
   arqSena.close()
   print ('Arquivo gerado')

principal()
