import MetaTrader5 as mt5
from datetime import datetime
import pytz
import pandas as pd
from decimal import Decimal

# Conectar ao MetaTrader 5
if not mt5.initialize():
    print("Falha na inicialização do MetaTrader 5")
    exit(1)

symbol = "EURUSD"  # Obter o símbolo desejado
timeframe = mt5.TIMEFRAME_M5  # Obter o timeframe desejado (M1, M5, H1, etc.)
data = datetime(2023, 6, 20, hour=15, minute=30, tzinfo=pytz.timezone("Etc/UTC"))  # Obter a data
current_candle = mt5.copy_rates_from(symbol, timeframe, data, 1)  # Obter a vela atual
# Exibir informações da vela atual
pd.set_option('display.max_columns', 500)  # número de colunas
pd.set_option('display.width', 1500)  # largura máxima da tabela
# Traduzindo e buscando apenas as colunas desejadas
dataFrame = pd.DataFrame(current_candle)
dataFrame['time'] = pd.to_datetime(dataFrame['time'], unit='s')
new_df = {'Data':       dataFrame['time'],
          'Abertura':   dataFrame['open'],
          'Máxima':     dataFrame['high'],
          'Mínima':     dataFrame['low'],
          'Fechamento': dataFrame['close'],
          'Volume':     dataFrame['tick_volume']}
print(pd.DataFrame(new_df))

########### CALCULO ############
# sparar as vars para calculo
CAL_max = new_df['Máxima']
CAL_min = new_df['Mínima']
CAL_Open = new_df['Abertura']
CAL_Close = new_df['Fechamento']
# Remover os valores de <class 'pandas.core.series.Series'>
CAL_max = CAL_max.drop(columns='Máxima')
CAL_min = CAL_min.drop(columns='Mínima')
CAL_Open = CAL_Open.drop(columns='Abertura')
CAL_Close = CAL_Close.drop(columns='Fechamento')

# deferença entre maxina e minima
CAL_diferenca_M_m = CAL_max - CAL_min
print(CAL_diferenca_M_m)

# deferença entre Abertura e Fechamento
CAL_diferenca_O_C = CAL_Close - CAL_Open
print(CAL_diferenca_O_C)

# porcentagem da diferença de Open e Close diante do total Max e Min
porcent = (CAL_diferenca_O_C * 100) / CAL_diferenca_M_m
print(porcent)
# posição da porcentagem na max e min
half = CAL_diferenca_M_m / 2
pos_percent = CAL_max - half
print(pos_percent)

# Desconectar do MetaTrader 5
mt5.shutdown()
