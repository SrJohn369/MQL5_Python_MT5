import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

# Inicializar a conexão com o terminal do MetaTrader 5
if not mt5.initialize():
    print("Erro ao inicializar MetaTrader 5")
    exit(-1)

# Variáveis Globais
# import pytz module for working with time zone
import pytz
time_zone = pytz.timezone('etc/UTC')
# Obter a data atual
data_atual = datetime(datetime.now().year, datetime.now().month, datetime.now().day, tzinfo=time_zone)

# Verificar se o dia é igual a 1
if data_atual.day == 1:
    # Verificar se o mês é igual a 1 (janeiro)
    if data_atual.month == 1:
        # Obter o dia anterior como o último dia de dezembro do ano anterior
        dia_anterior = 31
        mes_anterior = 12
        ano_anterior = data_atual.year - 1
        data = datetime(ano_anterior, mes_anterior, dia_anterior)
    else:
        # Obter o último dia do mês anterior
        ultimo_dia_mes_anterior = data_atual - timedelta(days=1)
        dia_anterior = ultimo_dia_mes_anterior.day
        mes_anterior = ultimo_dia_mes_anterior.month
        ano_anterior = data_atual.year
        data = datetime(ano_anterior, mes_anterior, dia_anterior)
else:
    # Obter o dia anterior
    dia_anterior = data_atual.day - 1
    mes_anterior = data_atual.month
    ano_anterior = data_atual.year
    data = datetime(ano_anterior, mes_anterior, dia_anterior)

# Obter os dados históricos de preços usando a função MT5CopyRatesFrom()
rates = mt5.copy_rates_from('XAUUSD', mt5.TIMEFRAME_M5, data_atual, 276)

# Imprimir os dados históricos de preços
for rate in rates:
    print(f"Data: {pd.Timestamp.fromtimestamp(rate[0])},"
          f" Abertura: {rate[1]}, Maxima:{rate[2]}"
          f" Fechamento: {rate[4]}, Minima: {rate[3]}"
          f" Spreed: {rate[6]}, Volume: {rate[5]}")
