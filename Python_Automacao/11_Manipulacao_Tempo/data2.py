from datetime import datetime, timedelta

hoje = datetime.now()
um_dia = timedelta(days=1) # representa o intervalo de um dia

amanha = hoje + um_dia
print(amanha)

ontem = hoje - um_dia
print(ontem)

prazo = datetime(2026, 3, 24)
if hoje > prazo:
    print("Prazo expirado")
else:
    print("Prazo não expirado")

futuro = datetime(2026, 3, 24)
dias_restantes = futuro - hoje
print(dias_restantes.days)

teste = datetime.strptime("01/01/2025", "%d/%m/%Y")
print(teste)