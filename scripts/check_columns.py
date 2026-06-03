import pandas as pd

print("TRANSACTIONS COLUMNS:")
print(pd.read_csv("data/processed/investor_transactions_cleaned.csv").columns)

print("\nPERFORMANCE COLUMNS:")
print(pd.read_csv("data/processed/scheme_performance_cleaned.csv").columns)