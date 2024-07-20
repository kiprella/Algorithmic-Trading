import pandas as pd

def sma(data, days):
    data['SMA'] = data['Close'].rolling(window=days).mean()
    return data


