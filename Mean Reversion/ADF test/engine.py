import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# ADF test 
#csv file need to be in data folder
test = input("Enter dataset name: ")
data = pd.read_csv('./data/'+test)

# Ignore NaN values 
prices = data['Close'].dropna()
result = adfuller(prices)



print(f'ADF Statistic: {result[0]}')

print(f'p-value: {result[1]}')
# if p-value <= 0.05  indicates strong evidence against the null hypothesis - series is stationary

print('Critical Values:', result[4])


# if result[0] < result[4]['5%']:
#     print("Series is likely stationary")
#     # AKA mean reversion strategy could possibly work
# else: 
#     print("Series is likely non-stationary")

# USDCAD.csv is not stationary
# Enter dataset name: USDCAD.csv
# ADF Statistic: -1.6536349919287192
# p-value: 0.4551453647528598
# Critical Values: {'1%': -3.431603356058229, '5%': -2.862093852984781, '10%': -2.5670648157322997}
# Series is likely non-stationary
# ADF statistic > 5% critical value, suggesting that the series is non-stationary


# Enter dataset name: VIX.csv
# ADF Statistic: -6.892035570356753
# p-value: 1.3479540617342404e-09
# Critical Values: {'1%': -3.4311190188723706, '5%': -2.861879854023006, '10%': -2.566950899393073}
# Series is likely stationary

