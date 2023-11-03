import pandas as pd
import statsmodels.api as sm
import numpy as np

# Load the data
data = pd.read_csv('VIX.csv')  # replace with your CSV path

# Calculate returns
data['returns'] = data['Close'].pct_change()
returns = data['returns'].dropna()

# Setup X and Y for regression
X = returns[1:].values.reshape(-1, 1)
X_lagged = returns[:-1].values.reshape(-1, 1)

# OLS regression to determine theta and mu
model = sm.OLS(X, X_lagged).fit()

# Print the regression parameter to diagnose the issue
print(f"Regression Parameter: {model.params[0]}")

# Ensure the regression parameter is positive before calculating theta and mu
if model.params[0] > 0:
    theta = -np.log(model.params[0])
    mu = model.params[0] / (1 - np.exp(-theta))
    print(f"Theta (speed of mean reversion): {theta}")
    print(f"Mu (long-term mean): {mu}")
else:
    print("The regression parameter is non-positive. Cannot compute theta and mu.")
