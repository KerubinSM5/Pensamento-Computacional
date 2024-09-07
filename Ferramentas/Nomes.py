def escrever():
   arqTxt = open('nomes.txt', 'w')
   continuar = True
   while continuar:
       nome = input('Digite um nome [Vazio-Sai]: ')
       if nome == '':
           continuar = False
           break
       arqTxt.write(nome + "\r")
   arqTxt.close()
   print ('Fim de escrita do arquivo')

def ler():
   arqTxt = open('nomes.txt', 'r')
   print ('Lista de nomes do arquivo:')
   for nome in arqTxt:
       print (nome, end='')
   arqTxt.close()
   print('Fim de leitura do arquivo')

escrever()
ler()
