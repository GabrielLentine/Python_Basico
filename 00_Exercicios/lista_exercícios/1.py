# um programa p/ calcular o estoque médio de uma peça (estoque médio = (qtd mínima + qtd máxima) / 2)
qtd_minima = int(input("Quantidade mínima em estoque: "))
qtd_maxima = int(input("Quantidade máxima em estoque: "))
estoque_medio = (qtd_minima + qtd_maxima) / 2

print(f"O estoque médio é de {round(estoque_medio)}")
