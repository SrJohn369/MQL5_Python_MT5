import MetaTrader5 as mt5

# Conecte-se ao MetaTrader 5
if not mt5.initialize():
    print("Falha ao conectar ao MetaTrader 5")
    exit()
