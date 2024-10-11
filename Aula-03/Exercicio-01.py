import util.Inputs as fi

nota1 = fi.input_int('Digite a primeira nota', 0,10)
nota2 = fi.input_int('Digite a segunda nota', 0,10)
nota3 = fi.input_int('Digite a terceira nota', 0,10)

media = ((nota1 + nota2 + nota3) / 3)

mencao = ''
if media == 0 and media < 5:
    mencao = 'Reprovado'
elif media >= 5:
    mencao = 'aprovado'

print(mencao, f'com média: {media}')