import pandas as pd
import matplotlib.pyplot as plt
from Indicator_Simple_moving_average import sma
from Indicator_Exponential_moving_average import ema
import numpy as np

## Read data file that you wish to strategy test
data = pd.read_csv('^GSPC_1995-01-01_2024-07-18.csv', parse_dates=['Date'], index_col='Date')


def wma(series, length):
    weights = np.arange(1, length + 1)
    return series.rolling(window=length).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)

def hma(series, length):
    half_length = length // 2
    sqrt_length = int(np.sqrt(length))
    wma1 = wma(series, half_length)
    wma2 = wma(series, length)
    return wma(2 * wma1 - wma2, sqrt_length)

Simple_moving_average = sma(data, 50)
EMA10= ema(data, 10)
EMA12= ema(data, 12)
EMA20= ema(data, 20)
EMA26= ema(data, 26)


## MACD Indicator
data['MACD'] = EMA12['EMA-12']-EMA26['EMA-26']
data['MACD Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

# Calculate Hull Moving Average (HMA)
hma_length = 55  # Example length, adjust as needed
data['HMA'] = hma(data['Close'], hma_length)



# Generate Buy and Sell Signals on given indicators
data['Buy Signal'] = (data['MACD'] > data['MACD Signal']) & (data['MACD'].shift(1) <= data['MACD Signal'].shift(1)) & (data['Close'] > data['HMA'])
data['Sell Signal'] = (data['MACD'] < data['MACD Signal']) & (data['MACD'].shift(1) >= data['MACD Signal'].shift(1)) & (data['Close'] < data['HMA'])



signals = []
holding = False
entry_price = None
entry_date = None

for index, row in data.iterrows():
    if row['Buy Signal'] and not holding:
        # Record the buy signal
        entry_price = row['Close']
        entry_date = index
        holding = True
        signals.append({'Date': entry_date, 'Type': 'Buy', 'Entry Price': entry_price, 'Exit Price': None, 'Profitability': None})
    
    elif row['Sell Signal'] and holding:
        # Record the sell signal
        exit_price = row['Close']
        # Profit = 1, Loss = 0
        profitability = 1 if exit_price > entry_price else 0
        signals.append({'Date': index, 'Type': 'Sell', 'Exit Price': exit_price, 'Profitability': profitability})
        holding = False

signals_df = pd.DataFrame(signals)
signals_df.to_csv('results.csv', index=False)


plt.figure(figsize=(10,10))

plt.subplot(2,1,1)
plt.plot(data.index, data['Close'], label='Close Price', color='blue')
# plt.plot(data.index, Simple_moving_average['SMA'], label='SMA', color='red')
# plt.plot(data.index, EMA10['EMA-10'], label='EMA-10', color='black')
# plt.plot(data.index, EMA12['EMA-12'], label='EMA-12', color='pink')
# plt.plot(data.index, EMA20['EMA-20'], label='EMA-20', color='green')
# plt.plot(data.index, EMA26['EMA-26'], label='EMA-26', color='yellow')
plt.scatter(data.index[data['Buy Signal']], data['Close'][data['Buy Signal']], marker='^', color='blue', label='Buy Signal', s=100, edgecolor='black')
plt.scatter(data.index[data['Sell Signal']], data['Close'][data['Sell Signal']], marker='v', color='red', label='Sell Signal', s=100, edgecolor='black')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price and Simple Moving Average')
plt.legend()
plt.grid(True)


plt.subplot(2,1,2)
plt.plot(data.index, data['MACD'], label='MACD', color='green', linewidth=1)
plt.plot(data.index, data['MACD Signal'], label='MACD Signal', color='red', linestyle='--', linewidth=1)


# y axis limits
plt.ylim(-10000,10000)
plt.axhline(0)

plt.xlabel('Date')
plt.ylabel('MACD')
plt.title('MACD and MACD Signal')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()