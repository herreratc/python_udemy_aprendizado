# somas e subtração.

#validação entrada
entrada = input('Para somar digite + para substrair digite - Para sair digite sair : ')


#funções
def calculo (x, y):
    if entrada == '+':
        return (x + y)
    elif entrada == '-':
        return (x - y)


#valores
valor1 = input('Digite o valor 1 :')
valor2 = input('Digite o valor 2 :')
v1 = int(valor1)
v2 = int(valor2)

resultado = calculo(v1, v2)
print(resultado)

while v1 and v2 > 0:
    entrada

    if entrada == 'sair':
        break