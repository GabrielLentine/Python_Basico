# hora atual com condições
from datetime import datetime

hora_atual = datetime.now()
if hora_atual.hour >= 6 and hora_atual.hour < 12:
    print("Bom dia!")
elif hora_atual.hour >= 12 and hora_atual.hour < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")

print(hora_atual.strftime("%H:%M:%S"))

# quantos meses faltam p/ o ano acabar
data_atual = datetime.now()
meses_restantes = 12 - data_atual.month
print(f"O mês atual é {data_atual.month} e faltam {meses_restantes} meses p/ o ano acabar")

# assinatura digital
def assinatura(nome):
    return f"Assinatura gerada por {nome} em {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}"

print(assinatura("Gabriel Lentine"))
