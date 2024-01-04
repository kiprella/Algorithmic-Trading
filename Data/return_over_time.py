import pandas as pd

file_name = input('Enter dataset: ')

df = pd.read_csv(file_name)
open_value = df['Open']
close_value = df['Close']

x = open_value.iloc[0]
y = close_value.iloc[-1]

price_change = x - y
asset_return = (y/x -1)*100

print(f"Asset return is: {asset_return:.2f}%")