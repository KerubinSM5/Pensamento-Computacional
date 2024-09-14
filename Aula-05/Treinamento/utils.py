import random

class aleatorio:
    def numeros_megasena(num, inicio, fim):
       lista = []
       numeros = 0
       continuar = True
       while continuar:
           aleatorio = random.randrange(inicio, fim) #gera numeros aleatórios
           if aleatorio not in lista: #verifica se um numero sorteado pertence ou não à lista; #Not in: não permite repetição de numero numa sequencia (linha)
               lista.append(aleatorio)
               numeros += 1
               if numeros == num:
                   continuar = False
       return lista