from datetime import datetime, timedelta

# Obter a data atual
data_atual = datetime(datetime.now().year, 1, 1)

# Verificar se o dia é igual a 1
if data_atual.day == 1:
    # Verificar se o mês é igual a 1 (janeiro)
    if data_atual.month == 1:
        # Obter o dia anterior como o último dia de dezembro do ano anterior
        dia_anterior = 31
        mes_anterior = 12
        ano_anterior = data_atual.year - 1
    else:
        # Obter o último dia do mês anterior
        ultimo_dia_mes_anterior = data_atual - timedelta(days=1)
        dia_anterior = ultimo_dia_mes_anterior.day
        mes_anterior = ultimo_dia_mes_anterior.month
        ano_anterior = data_atual.year
else:
    # Obter o dia anterior
    dia_anterior = data_atual.day - 1
    mes_anterior = data_atual.month
    ano_anterior = data_atual.year

print(data_atual.replace(day=1))
print(timedelta(days=1))
print(f"Data atual: {data_atual.day}/{data_atual.month}/{data_atual.year}")
print(f"Dia anterior: {dia_anterior}/{mes_anterior}/{ano_anterior}")
