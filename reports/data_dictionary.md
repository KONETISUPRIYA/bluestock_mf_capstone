# Data Dictionary

## fund_master

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund Company |
| scheme_name | Text | Mutual Fund Scheme Name |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |

## nav_history

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

## investor_transactions

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor Identifier |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Investment Amount |
| state | Text | Investor State |
| kyc_status | Text | KYC Verification Status |

## scheme_performance

| Column | Data Type | Description |
|----------|----------|----------|
| return_1yr_pct | Float | 1 Year Return |
| return_3yr_pct | Float | 3 Year Return |
| return_5yr_pct | Float | 5 Year Return |
| expense_ratio_pct | Float | Expense Ratio |
| aum_crore | Float | Assets Under Management |