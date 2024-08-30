'''Atribua o valor 10 à variável “x”
Atribua o valor 20 à variável “y”
Atribua o valor 30 à variável “z”
Verifique se “x” multiplicado por 3 é igual a “z” - teste booleano
Verifique se “z” é maior que a soma de “x” e “y” - teste booleano
Verifique se “z” subtraído de “y” é igual a “x” - teste booleano
'''

x = 10
y = 20
z = 30

teste1 = ((x * 3) == z)
teste2 = ((x + y)> z)
teste3 = ((z - y) == x)

print(teste1)
print(teste2)
print(teste3)