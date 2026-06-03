import pandas as pd

# -----------------------
# NAV HISTORY CLEANING
# -----------------------

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[nav_df["nav"] > 0]

nav_df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("NAV History Cleaned")


# -----------------------
# INVESTOR TRANSACTIONS
# -----------------------

txn_df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

txn_df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions Cleaned")


# -----------------------
# SCHEME PERFORMANCE
# -----------------------

perf_df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

perf_df = perf_df[
    (perf_df["expense_ratio_pct"] >= 0.1)
    &
    (perf_df["expense_ratio_pct"] <= 2.5)
]

perf_df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance Cleaned")

print("All Cleaning Completed Successfully")