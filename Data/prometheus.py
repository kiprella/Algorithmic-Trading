import yfinance as yf

ticker = ['X','Y','Z']
# YEAR-MONTH-DAY
# XXXX-XX-XX
date_x = '2018-01-01'
date_y = '2024-06-08'


def test_yfinance():
    for symbol in ticker:
        # print(">>", symbol, end=' ... ')
        data = yf.download(symbol,start=date_x, end=date_y)
        csv_filename = f"{symbol}_data.csv"
        data.to_csv(csv_filename)
        print(data)


if __name__ == "__main__":
    test_yfinance()

#                   Open        High         Low       Close   Adj Close     Volume
# Date
# 2020-09-25  108.430000  112.440002  107.669998  112.279999  110.286530  149981400
# 2020-09-28  115.010002  115.320000  112.779999  114.959999  112.918945  137672400
# 2020-09-29  114.550003  115.309998  113.570000  114.089996  112.064392   99382200
# 2020-09-30  113.790001  117.260002  113.620003  115.809998  113.753845  142675200
# 2020-10-01  117.639999  117.720001  115.830002  116.790001  114.716469  116120400