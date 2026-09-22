print("Bem-vindo à classificação de filmes")
print("Você terá 5 filmes para classificar")

classificacoes = []

for contador in range(1, 6):

    classificacao = input(f"Como você classifica o filme {contador}?: ")
    classificacao = int(classificacao)

    if classificacao == 0:
        print("Sessão encerrada")
        break

    if classificacao < 1 or classificacao > 5:
        print("Classificação inválida") 
    else:
        classificacoes.append(classificacao)
        print(f"Você classificou o filme {contador} com a nota {classificacao}")


print("Lista de filmes classificados:")

for i in range(1, len(classificacoes) + 1):
    print(f"Filme {i}: Classificação {classificacoes[i - 1]}")

   