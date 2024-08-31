#Recebe um texto, não aceitando texto vazio
def input_texto(msg):
    texto = ''
    while texto == '':
        texto = input(msg + ': ')
    return texto

#Verifica se são dígitos inteiros
def sao_digitos(entrada):
    e_numero = True

    if entrada[0] == '-': #verifica se tem um sinal negativo na primeira posição para aceitar numeros negativos
        processar = entrada[1:len(entrada)]
    else:
        processar = entrada

    for digito in processar:  # "Filtra" dígitos inteiros de outros caracteres
        if digito not in '0123456789':
            e_numero = False
    return e_numero

def limites(minimo, maximo, valor):
    if valor >= minimo and valor <= maximo:
        return True
    else:
        return False

#Recebe um numero inteiro entre um minimo e um máximo
def input_int(msg, minimo, maximo): #limita as possibilidades de valores inteiros para valores mínimo e máximo definidos
    receber =  True
    numero = 0
    while receber:
        entrada = input_texto(msg)

        if not sao_digitos(entrada): #informa digitos inteiros*
            print("Digito não inteiro")
        else:
            numero = int(entrada)
            if limites(minimo, maximo, numero):
                receber = False
            else:
                print("Você tem que digitar um numero entre {} e {}".format(minimo,maximo))
            receber = False
    return numero
