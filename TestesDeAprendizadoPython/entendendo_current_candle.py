import MetaTrader5 as mt5
from datetime import datetime
import pytz
import pandas as pd

# Conectar ao MetaTrader 5
if not mt5.initialize():
    print("Falha na inicialização do MetaTrader 5")
    exit(1)

symbol = "XAUUSD"  # Obter o símbolo desejado
timeframe = mt5.TIMEFRAME_M5  # Obter o timeframe desejado (M1, M5, H1, etc.)
data = datetime(2023, 6, 20, hour=15, minute=20, tzinfo=pytz.timezone("Etc/UTC"))  # Obter a data
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
cal_MAX = new_df['Máxima'].values[0]
cal_MIN = new_df['Mínima'].values[0]
cal_OPEN = new_df['Abertura'].values[0]
cal_CLOSE = new_df['Fechamento'].values[0]


# deferença entre maxina e minima
def def_MAX_MIN():
    return cal_MAX - cal_MIN


# deferença entre Abertura e Fechamento
def def_Open_Close():
    return cal_OPEN - cal_CLOSE


# Identifica se é baixa(0) ou alta(1)
def identificaVela():
    if cal_CLOSE > cal_OPEN:
        return 1
    elif cal_CLOSE < cal_OPEN:
        return 0


# quantos porcentos tem a deferença entre Abertura e Fechamento da candle
# a diferença entre Open e Close é a candle inteira
def porcentVela():
    return (def_Open_Close() * 100) / def_MAX_MIN()


# Dados da candle
def dadosCandle():
    # baixa
    if identificaVela() == 0:
        def_Max_Open = cal_MAX - cal_OPEN
        def_Close_Min = cal_CLOSE - cal_MIN
        return def_Max_Open, def_Close_Min
    elif identificaVela() == 1:
        def_Open_Min = cal_OPEN - cal_MIN
        def_Max_Close = cal_MAX - cal_CLOSE
        return def_Open_Min, def_Max_Close


print(def_MAX_MIN(), "maxima e minima")
print(def_Open_Close(), "Abertura e fechamento")
print(identificaVela(), "Baixa" if identificaVela() == 0 else "Alta")
print(porcentVela(), "Porcentagem")
print(dadosCandle(), "Dados Candle")

# Desconectar do MetaTrader 5
mt5.shutdown()
