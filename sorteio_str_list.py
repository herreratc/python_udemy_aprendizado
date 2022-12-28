#Sorteio utilizando entradas de str convertendo em list


#IMPORTAÇÃO RANDOM
import random


#INTRO
print()
print('Bem vindo ao sorteiro! Digite o nome de 4 participas para sortear.')
print()

#ENTRADAS
p1 = str(input('Digite o nome do participante: '))
p2 = str(input('Digite o nome do proximo participante: '))
p3 = str(input('Digite o nome do 3 participante: '))
p4 = str(input('Digite o nome do 4 participante: '))

#CONVERTENDO EM LIST
lista = [p1,p2,p3,p4]

#RESULTADO
print()
print('O sorteado 1 foi {}!'.format(random.choice(lista)))
