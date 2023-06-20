import MetaTrader5 as mt5

# Conectar ao MetaTrader 5
if not mt5.initialize():
    print("Falha na inicialização do MetaTrader 5")
    exit(1)

# Obter o símbolo desejado
symbol = "EURUSD"

# Obter o timeframe desejado (M1, M5, H1, etc.)
timeframe = mt5.TIMEFRAME_M5

# Obter a vela atual
current_candle = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1)[0]

# Exibir informações da vela atual
print("Vela atual:")
print("Abertura:", current_candle[1])
print("Máxima:", current_candle[2])
print("Mínima:", current_candle[3])
print("Fechamento:", current_candle[4])

# Desconectar do MetaTrader 5
mt5.shutdown()
