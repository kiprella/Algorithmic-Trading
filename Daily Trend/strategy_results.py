import pandas as pd

# Load the CSV file with trading signals and profitability
signals_df = pd.read_csv('buy_sell_signals_with_profitability.csv')

# Convert Profitability to float if not already (to ensure proper counting)
signals_df['Profitability'] = signals_df['Profitability'].astype(float)

# Count the occurrences of each profitability value
profit_count = signals_df['Profitability'].value_counts()

# Print the counts
print(f"Number of profitable trades (Profitability = 1.0): {profit_count.get(1.0, 0)}")
print(f"Number of losing trades (Profitability = 0.0): {profit_count.get(0.0, 0)}")
