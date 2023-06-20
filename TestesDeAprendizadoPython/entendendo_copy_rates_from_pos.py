from datetime import datetime
import MetaTrader5 as mt5

# exibimos dados sobre o pacote MetaTrader5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# importamos o módulo pandas para exibir os dados recebidos na forma de uma tabela
import pandas as pd

pd.set_option('display.max_columns', 500)  # número de colunas
pd.set_option('display.width', 1500)  # largura máxima da tabela

# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# solicitamos 10 barras de GBPUSD D1 do dia atual
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M5, 1, 286)

# concluímos a conexão ao terminal MetaTrader 5
mt5.shutdown()

# exibimos cada elemento de dados recebidos numa nova linha
print("Exibimos os dados recebidos como estão")
for rate in rates:
    print(rate)

# a partir dos dados recebidos criamos o DataFrame
rates_frame = pd.DataFrame(rates)
# convertemos o tempo em segundos no formato datetime
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# exibimos dados
print("\nExibimos o dataframe com dados")
print(rates_frame)