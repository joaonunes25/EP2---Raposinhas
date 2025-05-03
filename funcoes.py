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