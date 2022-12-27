import os

lista_completa = []

while True:
    print('Bem vindo! Digite [I]nserir [A]pagar [L]istar:')
    opcao = input('Digite a opção desejada: ')
 
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_completa.append(valor)

    elif opcao == 'a':
        indice_lista = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_lista)
            del lista_completa[indice]
        except ValueError:
            print('Por favor digite um numero inteiro')
        except IndexError:
            print('Indice não existe na lista de compras')
        except Exception:
            print('Erro desconhecido')
            
    elif opcao == 'l':
        os.system('cls')

        if len(lista_completa) == 0:
            print('Nada para mostrar')
        
        for i, valor in enumerate(lista_completa):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')