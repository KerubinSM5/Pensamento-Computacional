#entrada
nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
peso1 = float(input('Qual o primeiro peso: '))
peso2 = float(input('Qual o segundo peso: '))

#Processamento / calculo
mp = ((nota1*peso1) + (nota2*peso2)) / (peso1 + peso2)

#Saída

print('A media ponderada foi {:.2f} '.format(mp))