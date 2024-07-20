import pandas as pd
import matplotlib.pyplot as plt
from Indicator_Simple_moving_average import sma
from Indicator_Exponential_moving_average import ema

data = pd.read_csv('BTC-USD_2015-01-01_2024-07-18.csv', parse_dates=['Date'], index_col='Date')



Simple_moving_average = sma(data, 50)
EMA10= ema(data, 10)
EMA12= ema(data, 12)
EMA20= ema(data, 20)
EMA26= ema(data, 26)



plt.figure(figsize=(10,30))

# plt.subplot(2,1,1)
plt.plot(data.index, data['Close'], label='Close Price', color='blue')
plt.plot(data.index, Simple_moving_average['SMA'], label='SMA', color='red')
plt.plot(data.index, EMA10['EMA-10'], label='EMA-10', color='black')
plt.plot(data.index, EMA12['EMA-12'], label='EMA-12', color='pink')
plt.plot(data.index, EMA20['EMA-20'], label='EMA-20', color='green')
plt.plot(data.index, EMA26['EMA-26'], label='EMA-26', color='yellow')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price and Simple Moving Average')

plt.legend()
plt.show()


