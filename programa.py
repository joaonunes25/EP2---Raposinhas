from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

cart_regra_simples = ['1', '2', '3', '4', '5', '6']
cart_regra_avanc = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

rodadas = 0

while rodadas < 12:
    rerrolagens = 0
    dados_guard = []
    dados_rolados = rolar_dados(5)
    cont = True

    while cont:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guard}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        num = input()
        while num not in ['1', '2', '3', '4', '0']:
            print('Opção inválida. Tente novamente.')
            num = input()
            
        if num == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            result = guardar_dado(dados_rolados, dados_guard, indice)
            dados_rolados, dados_guard = result

        elif num == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            result = remover_dado(dados_rolados, dados_guard, indice)
            dados_rolados, dados_guard = result

        elif num == '3':
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif num == '4':
            imprime_cartela(cartela)

        elif num == '0':
            dados = dados_guard + dados_rolados
            print('Digite a combinação desejada:')
            while True:
                combinacao = input()
                if combinacao in cart_regra_simples:
                    if cartela['regra_simples'][int(combinacao)] == -1:
                        cartela = faz_jogada(dados, combinacao, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                elif combinacao in cart_regra_avanc:
                    if cartela['regra_avancada'][combinacao] == -1:
                        cartela = faz_jogada(dados, combinacao, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            cont= False
            

    rodadas += 1

imprime_cartela(cartela)
pontuacao_final = 0
pontos_simples = sum(valor for valor in cartela['regra_simples'].values() if valor != -1)
pontos_avancada = sum(valor for valor in cartela['regra_avancada'].values() if valor != -1)
pontuacao_final = pontos_simples + pontos_avancada

if pontos_simples >= 63:
    pontuacao_final += 35


print(f"Pontuação total: {pontuacao_final}")