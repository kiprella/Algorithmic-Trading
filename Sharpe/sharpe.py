def SharpeRatio(rp,rf, qp):
    #Rp - expected portfolio return
    #Rf - risk-free rate of return
    #Qp - standard deviaton of the portfolio's excess return (portfolio's volatility) 
    sharpe = (rp-rf)/qp
    return sharpe


# print(SharpeRatio(0.08,0.02,0.10))
# Rp - 8%
# Rf - 2%
# Qp - 10%


# As a rule of thumb, any strategy that has a Sharpe ratio of less
# than 1 is not suitable as a stand-alone strategy. For a strategy that
# achieves profitability almost every month, its (annualized) Sharpe
# ratio is typically greater than 2. For a strategy that is profitable
# almost every day, its Sharpe ratio is usually greater than 3.

# - Quantitative trading (Ernest P. Chan)

