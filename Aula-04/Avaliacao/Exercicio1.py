def registra():
    dados = []
    try:
        ler = open('ex1.txt', 'r')
        dados = ler.readlines()
        ler.close()
    except FileNotFoundError:
        print('Primeira gravação')
    arq = open('ex1.txt', 'w')
    for linha in dados:
        arq.write(linha)
    nome = input('Qual o nome para registro? ')
    arq.write(nome + '\n')
    arq.close()


def lista():
    arq = open('ex1.txt', 'r')
    for nome in arq:
        print(nome, end='')
    arq.close()


def html():
    parte_fixa1 = '''
    <!DOCTYPE html>
<html lang="pt-br">


<head>
    <meta charset="utf-8">
    <title>Tabela</title>
    <style>
        th,
        td {
            border: 2px solid blue;
            background-color: #eeeeff;
        }
    </style>
</head>


<body>
    <h1 style="text-align: center;">Tabela com Nomes</h1>
    <hr />
    <br />


    <table style="width:100%; margin:auto; border-collapse: collapse;">
        <tr>
            <th>Número</th>
            <th>Nome</th>
        </tr>

        '''
    parte_fixa2 = '''
       </table>
       </body>
       </html>
        '''
    arqHTML = open('ex1.html', 'w')
    arqHTML.write(parte_fixa1)

    arq = open('ex1.txt', 'r')
    numero = 1
    for nome in arq:
        print('Gerando linha para', nome)
        arqHTML.write('''
        <tr>
            <td>{}</td>
            <td>{}</td>
        </tr>
        '''.format(numero, nome))
        numero += 1
    arq.close()
    arqHTML.close()


sair = False
while not sair:
    print('\n' * 2)
    print('1 - Registrar nome')
    print('2 - Listar nomes')
    print('3 - Gerar HTML')
    print('4 - Sair')
    opc = int(input('Qual a opção? '))
    if opc == 1:
        registra()
    elif opc == 2:
        lista()
    elif opc == 3:
        html()
    elif opc == 4:
        sair = True
    else:
        print("Opção inválida!")
