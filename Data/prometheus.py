import yfinance as yf
import csv

ticker = '^GSPC'
start_date = '1995-01-01'
end_date = '2024-07-18'





data = yf.download(ticker, start=start_date, end=end_date)

data.to_csv(f"{ticker}_{start_date}_{end_date}.csv")



#                   Open        High         Low       Close   Adj Close     Volume
# Date
# 2020-09-25  108.430000  112.440002  107.669998  112.279999  110.286530  149981400
# 2020-09-28  115.010002  115.320000  112.779999  114.959999  112.918945  137672400
# 2020-09-29  114.550003  115.309998  113.570000  114.089996  112.064392   99382200
# 2020-09-30  113.790001  117.260002  113.620003  115.809998  113.753845  142675200
# 2020-10-01  117.639999  117.720001  115.830002  116.790001  114.716469  116120400