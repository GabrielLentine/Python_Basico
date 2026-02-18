# pagamento de comissão (5%) de vendedores de peça
# - id do vendedor
# - cód da peça
# - preço unitário da peça
# - qtd vendida

vendedor = {
    "id": 123,
    "name": "Gabriel",
}

peca = {
    "código": 123,
    "preço_unitario": 10.00
}

inpt_venda = int(input("Informe a quantidade vendida: "))
qtd_venda = peca["preço_unitario"] * inpt_venda

id_vendedor = int(input("Informe o ID do vendedor: "))
if id_vendedor == vendedor.get("id"):
    comissao = qtd_venda * 0.05
    print(f"Foram vendidas {inpt_venda} peças, cada uma está custando R${peca["preço_unitario"]} a unidade. Logo, sua comissão é de R${comissao:.2f}.")
