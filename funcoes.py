import random
def rolar_dados (num):
    lista = []
    for i in range(num):
        lista.append(random.randint(1,6))
    return lista

def guardar_dado (dados_rolados, dados_guard, num):
    lista = []
    dados_guard.append(dados_rolados[num])
    del dados_rolados[num]
    lista.append(dados_rolados)
    lista.append(dados_guard)
    return lista

def remover_dado(dados_rolados, dados_guard, dado_para_remover):
    lista = []
    dados_rolados.append(dados_guard[dado_para_remover])
    del dados_guard[dado_para_remover]
    lista.append(dados_rolados)
    lista.append(dados_guard)
    return lista

def calcula_pontos_regra_simples(lista):
    dicio = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(len(lista)):
        if lista[i] in dicio:
            dicio[lista[i]] += lista[i]
    return dicio

def calcula_pontos_soma(lista):
    i = 0
    soma = 0
    while i < len(lista):
        soma += lista[i]
        i += 1
    return soma

def calcula_pontos_sequencia_baixa(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 15
    if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 15
    return 0
        
def calcula_pontos_sequencia_alta (lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 30
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        return 30
    return 0

def calcula_pontos_full_house(lista):
    dicio = {}
    for i in range (len(lista)):
        if lista[i] in dicio:
            dicio[lista[i]] += 1
        elif lista[i] not in dicio:
            dicio[lista[i]] = 1

    lista2 = []

    for item in dicio:
        lista2.append(item)
    
    if len(lista2) == 2:
        return sum(lista)
    else:
        return 0

