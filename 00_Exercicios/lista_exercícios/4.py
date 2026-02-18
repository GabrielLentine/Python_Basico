# ler quatro valores inteiros e mostrar o resultado (dois a dois) da adição e multiplicação. (Ex.: A + B; A + C; A + D; A * B; A * C; A * D;)
valor_a = int(input("Digite um número: "))
valor_b = int(input("Digite um número: "))
valor_c = int(input("Digite um número: "))
valor_d = int(input("Digite um número: "))

def sum(valor_a, valor_b):
    return valor_a + valor_b

def mult(valor_a, valor_b):
    return valor_a * valor_b

print()

# adição
print(f"A soma de {valor_a, valor_b} é {sum(valor_a, valor_b)}")
print(f"A soma de {valor_a, valor_c} é {sum(valor_a, valor_c)}")
print(f"A soma de {valor_a, valor_d} é {sum(valor_a, valor_d)}")
print(f"A soma de {valor_b, valor_c} é {sum(valor_b, valor_c)}")
print(f"A soma de {valor_b, valor_d} é {sum(valor_b, valor_d)}")
print(f"A soma de {valor_c, valor_d} é {sum(valor_c, valor_d)}")

print()

# multiplicação
print(f"A multiplicação de {valor_a, valor_b} é {mult(valor_a, valor_b)}")
print(f"A multiplicação de {valor_a, valor_c} é {mult(valor_a, valor_c)}")
print(f"A multiplicação de {valor_a, valor_d} é {mult(valor_a, valor_d)}")
print(f"A multiplicação de {valor_b, valor_c} é {mult(valor_b, valor_c)}")
print(f"A multiplicação de {valor_b, valor_d} é {mult(valor_b, valor_d)}")
print(f"A multiplicação de {valor_c, valor_d} é {mult(valor_c, valor_d)}")
