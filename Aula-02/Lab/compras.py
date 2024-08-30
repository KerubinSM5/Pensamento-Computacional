#Base de dados em memória
#numero = 1
total = 0.0
produtos = []
valores= []
quantidades = []

#Entrada de produtos
continuar = True
while continuar:
    produto = input("Qual o produto? ") 
    valor = float(input("Qual o valor? "))
    qtd = int(input("Qual a quantidade? "))
    produtos.append(produto)
    valores.append(valor)
    quantidades.append(qtd)
    opc = input("Terminar? [S/N] ")
    continuar = not (opc == 'S' or opc == 's')

#Emissão da nota
indice = 0
quant = len(produtos)
while indice < quant:
    total_item = valores[indice] * quantidades[indice]
    total  += total_item
    print('{} - {} : {} * {} = {}'.format(indice+1, produtos[indice], valores[indice], quantidades[indice], total_item))

    indice += 1

print("Total da compra: R$ ", total)