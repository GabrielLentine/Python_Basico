# dólar - real
cotacao_dolar = float(input("Qual a cotação do dólar?: "))
valor_dolar = float(input("Digite o valor (em U$): "))
valor_reais = cotacao_dolar * valor_dolar

print(f"O valor U${valor_dolar:.2f} em R$ é R${valor_reais:.2f}.")
