
#Se par_impar for TRUE = par se for FALSE = impar
def par_impar(numero):
    operacao = numero % 2 == 0

    if operacao:
        return f'Seu número {numero} é par'
    else:
        return f'Seu número {numero} é impar'


valor1 = input('Digite um numero: ')
v1 = int(valor1)

print(par_impar(v1))
