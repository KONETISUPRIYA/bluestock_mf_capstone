-- 1. Top 5 Funds By AUM

SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Funds With Expense Ratio Less Than 1%

SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 3. Top 5 Funds By 5 Year Return

SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- 4. Average NAV By Fund

SELECT amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- 5. Highest NAV Recorded

SELECT amfi_code,
MAX(nav) AS highest_nav
FROM fact_nav
GROUP BY amfi_code;


-- 6. Transaction Count By Type

SELECT transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;


-- 7. Total Investment By Type

SELECT transaction_type,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 8. Transactions By State

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 9. KYC Status Distribution

SELECT kyc_status,
COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;


-- 10. Total Investment By City Tier

SELECT city_tier,
SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY city_tier;