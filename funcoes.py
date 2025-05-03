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
    i = 0
    while i < 2:
        if lista[i] == 1 and lista[i+1] == 2 and lista[i+2] == 3 and lista[i+3] == 4:
            return 15
        if lista[i+3] == 1 and lista[i+2] == 2 and lista[i+1] == 3 and lista[i] == 4:
            return 15
        if lista[i] == 2 and lista[i+1] == 3 and lista[i+2] == 4 and lista[i+3] == 5:
            return 15
        if lista[i+3] == 2 and lista[i+2] == 3 and lista[i+1] == 4 and lista[i] == 5:
            return 15
        if lista[i] == 3 and lista[i+1] == 4 and lista[i+2] == 5 and lista[i+3] == 6:
            return 15
        if lista[i+3] == 3 and lista[i+2] == 4 and lista[i+1] == 5 and lista[i] == 6:
            return 15
        i += 1
    return 0