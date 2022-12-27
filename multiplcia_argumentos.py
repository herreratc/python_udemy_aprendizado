# multiplcia_argumentos

def valores(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = valores(1, 2, 3, 4, 5)
print(resultado)