-- Transactions from high-risk countries
SELECT * FROM transactions
WHERE country_code IN ('XYZ', 'ABC');

-- Transactions at unusual hours
SELECT * FROM transactions
WHERE EXTRACT(HOUR FROM timestamp) NOT BETWEEN 6 AND 22;

-- Velocity checks: Transactions within a short period
SELECT account_id, COUNT(*) as transaction_count
FROM transactions
WHERE timestamp > NOW() - INTERVAL '1 HOUR'
GROUP BY account_id
HAVING COUNT(*) > 5;

-- Flag transactions below reporting thresholds
SELECT * FROM transactions
WHERE amount BETWEEN 9900 AND 10000;