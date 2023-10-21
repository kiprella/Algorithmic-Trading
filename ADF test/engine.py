import pandas as pd
from statsmodels.tsa.stattools import adfuller

# ADF test 
#csv file need to be in data folder
test = input("Enter dataset name: ")


data = pd.read_csv('./data/'+test)

# Ignore NaN values 
prices = data['Close'].dropna()

# ADF test
result = adfuller(prices)

print(f'ADF Statistic: {result[0]}')

print(f'p-value: {result[1]}')
# if p-value <= 0.05  indicates strong evidence against the null hypothesis - series is stationary

print('Critical Values:', result[4])

if result[0] < result[4]['5%']:
    print("Series is likely stationary")
    # AKA mean reversion strategy could possibly work
else: 
    print("Series is likely non-stationary")



