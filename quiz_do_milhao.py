 #SHOW DO MILHAO! 

#Importar sys para limpar a tela
import os

#Lista de perguntas
perguntas = [
    {
    'Pergunta': 'Quanto é 10 + 10 ?',
    'Opções': ['21', '12', '20', '40'],
    'Resposta': '20',
    },
    {
    'Pergunta': 'Quanto é 10 * 10 ?',
    'Opções': ['100', '1000', '200', '10'],
    'Resposta': '100',
    },
    {
    'Pergunta': 'Quanto é 100 / 10 ?',
    'Opções': ['50', '10', '2', '20'],
    'Resposta': '10',
    },

]


#Saudação
print('Bem vindo ao Show do Milhão! Teste seus conhecimentos!')

#NomeDoParticipante e saldo de pontos
nome = input('Digite seu nome para continuar: ')
saldo = 0 
saldo = (saldo)

os.system('cls')

#Iniciar as perguntas
print(nome, 'cada pergunta vale 10 pontos, se você acertar 3 voce ganha 1 milhão de reais!!!!')
iniciar = input('Para iniciar a primeira pergunta digite a letra [i] Para sair digite [sair]: ')

#Executar

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        saldo += 10
        print('Resposta correta', 'Seu saldo atual é: ', (saldo))
    else:
        print('Resposta errada', 'Seu saldo atual é: ', (saldo))

    print()



os.system('cls')

print('Você acertou', (saldo))
print('de', len(perguntas), 'perguntas.')


if saldo == '0':
    print('Você não acerto nada!! Não vai levar nenhum real')
elif saldo == '10':
    print('Só acerto 1, leva 1 real ')
elif saldo == '20':
    print('Quase ganho um milhão seu noia')
elif saldo == '30':
    print('Parabensssssssssssssssss, você ganho um milhão de reais')
