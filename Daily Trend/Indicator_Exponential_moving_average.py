import pandas as pd



def ema(data, days):
    data[f'EMA-{days}'] = data['Close'].ewm(span=days, adjust=False).mean()
    return data

    