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
        else:
            dicio[lista[i]] = 1
    
    if 2 in dicio.values() and 3 in dicio.values():
        soma = 0
        for i in range(len(lista)):
            soma += lista[i]
        return soma
    else:
        return 0
    
def calcula_pontos_quadra(lista):
    um = 0
    dois = 0
    tres = 0
    quatro = 0
    cinco = 0
    seis = 0
    i = 0
    soma = 0
    while i < len(lista):
        if lista[i] == 1:
            um += 1
        if lista[i] == 2:
            dois += 1
        if lista[i] == 3:
            tres += 1
        if lista[i] == 4:
            quatro += 1
        if lista[i] == 5:
            cinco += 1
        if lista[i] == 6:
            seis += 1
        soma += lista[i]
        i += 1
    
    if um >= 4 or dois >= 4 or tres >= 4 or quatro >= 4 or cinco >= 4 or seis >= 4:
        return soma
    else:
        return 0
    
def calcula_pontos_quina(lista):
    um = 0
    dois = 0
    tres = 0
    quatro = 0
    cinco = 0
    seis = 0
    i = 0
    soma = 0
    while i < len(lista):
        if lista[i] == 1:
            um += 1
        if lista[i] == 2:
            dois += 1
        if lista[i] == 3:
            tres += 1
        if lista[i] == 4:
            quatro += 1
        if lista[i] == 5:
            cinco += 1
        if lista[i] == 6:
            seis += 1
        soma += lista[i]
        i += 1
    
    if um >= 5 or dois >= 5 or tres >= 5 or quatro >= 5 or cinco >= 5 or seis >= 5:
        return 50
    else:
        return 0
    
def calcula_pontos_regra_avancada(lista):
    dicio = {
            'cinco_iguais': calcula_pontos_quina(lista),
            'full_house': calcula_pontos_full_house(lista), 
            'quadra': calcula_pontos_quadra(lista), 
            'sem_combinacao': calcula_pontos_soma(lista), 
            'sequencia_alta': calcula_pontos_sequencia_alta (lista), 
            'sequencia_baixa': calcula_pontos_sequencia_baixa(lista)
            }
    return dicio

def faz_jogada(lista, texto, dicio):
    texto = str(texto).strip()

    if texto in ['1', '2', '3', '4', '5', '6']:
        num = int(texto)
        pont = calcula_pontos_regra_simples(lista)
        if dicio['regra_simples'][num] == -1:  
            dicio['regra_simples'][num] = pont[num]
        else:
            print("Erro: Essa combinação já foi utilizada.")
    elif texto in dicio["regra_avancada"]:
        pont = calcula_pontos_regra_avancada(lista)
        if texto in pont: 
            if dicio["regra_avancada"][texto] == -1: 
                dicio["regra_avancada"][texto] = pont[texto]
            else:
                print("Erro: Essa combinação já foi utilizada.")
        else:
            print("Erro: Combinação inválida.")
    else:
        print("Erro: Opção inválida.")
    return dicio

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)