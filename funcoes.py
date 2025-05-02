import random
def rolar_dados (num):
    lista = []
    for i in range(num):
        lista.append(random.randint(1,6))
    return lista