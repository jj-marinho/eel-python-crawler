from forex_python.converter import CurrencyRates

c = CurrencyRates()

print(c.get_rate('USD', 'BRL'))