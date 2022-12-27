import os

lista_completa = []

while True:
    print('Bem vindo! Digite [I]nserir [A]pagar [L]istar:')
    opcao = input('Digite a opção desejada: ')
 
    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista_completa.append(valor)

