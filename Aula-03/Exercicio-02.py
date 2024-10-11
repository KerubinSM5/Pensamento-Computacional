#media ponderada - pesos: 1, 1.5 e 2
#Mostrar menção

#Exercício 02
import util.Inputs as fi

nota1 = fi.input_int('Digite a primeira nota',0,10)
nota2 = fi.input_int('Digite a segunda nota',0,10)
nota3 = fi.input_int('Digite a terceira nota',0,10)

mp = ((nota1 * 1) + (nota2 * 1.5) + (nota3 *2)) / (1 + 1.5 +2)
print('A média ponderada é', mp)

mencao = ''
if mp == 0:
    mencao = 'SR'
elif mp < 2:
    mencao = 'II'
elif mp < 5:
    mencao = 'MI'
elif mp < 7:
    mencao = 'MM'
elif mp < 9:
    mencao = 'MS'
else:
    mencao = 'SS'

print('Sua menção é: ', mencao)