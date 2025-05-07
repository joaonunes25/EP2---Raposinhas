from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'full_house': -1,
        'quadra': -1,
        'cinco_iguais': -1,
        'sem_combinacao': -1
    }
}

imprime_cartela(cartela)

cart_regra_simples = [1, 2, 3, 4, 5, 6]
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
        num = input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação')

        while num not in ['1', '2', '3', '4', '0']:
            print('Opção inválida. Tente novamente.')
            num = input('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação')
            
        if num == '1':
            try:
                num = int(input('Digite o índice do dado a ser guardado (0 a 4): '))
                if 0 <= num < len(dados_rolados):
                    result = guardar_dado(dados_rolados, dados_guard, num)
                    dados_rolados, dados_guard = result
                else:
                    print("Erro: Índice fora do intervalo. Tente novamente.")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número inteiro.")

        elif num == '2':
            try:
                dado_para_remover = int(input("Digite o índice do dado a ser removido (0 a 4): "))
                if 0 <= dado_para_remover < len(dados_guard):
                    result = remover_dado(dados_rolados, dados_guard, dado_para_remover)
                    dados_rolados, dados_guard = result
                else:
                    print("Erro: Índice fora do intervalo. Tente novamente.")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número inteiro.")
            
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
            jogada = input('Digite a combinação desejada:').strip()

            if jogada in ['1', '2', '3', '4', '5', '6']:
                jogada = int(jogada)
                if cartela['regra_simples'][jogada] == -1:
                    cartela = faz_jogada(dados, str(jogada), cartela)
                    cont = False
                else:
                    print("Essa combinação já foi utilizada.")
            elif jogada in cart_regra_avanc:
                if cartela['regra_avancada'][jogada] == -1:
                    cartela = faz_jogada(dados, jogada, cartela)
                    cont = False
                else:
                    print("Essa combinação já foi utilizada.")
            else:
                print("Combinação inválida. Tente novamente.")

    rodadas += 1

imprime_cartela(cartela)
pontos_simples = sum([v for v in cartela['regra_simples'].values() if v != -1])
pontos_avancados = sum([v for v in cartela['regra_avancada'].values() if v != -1])
bonus = 35 if pontos_simples >= 63 else 0
total = pontos_simples + pontos_avancados + bonus

print(f"Pontuação total: {total}")