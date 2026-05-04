-- Write your PostgreSQL query statement below
SELECT TO_CHAR(trans_date, 'yyyy-mm') AS month,
        country,
        COUNT(*) AS trans_count,
        COUNT(*) FILTER (WHERE state = 'approved') AS approved_count,
        SUM(amount) AS trans_total_amount,
        coalesce(SUM(amount) FILTER (WHERE state = 'approved'), 0) AS approved_total_amount
FROM Transactions
GROUP BY month, country





-- Write your PostgreSQL query statement below
SELECT
    TO_CHAR(trans_date, 'YYYY-MM') AS month,
    country,
    COUNT(*) AS trans_count,
    COUNT(
        CASE
            WHEN state = 'approved' THEN 1
            ELSE null
        END
    ) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(
        CASE
            WHEN state = 'approved' THEN amount
            ELSE 0
        END
    ) AS approved_total_amount
FROM Transactions
GROUP BY 
    TO_CHAR(trans_date, 'YYYY-MM'),
    country;


SELECT to_char(trans_date,'YYYY-MM') AS month, country, COUNT(trans_date) AS trans_count, 
COUNT(CASE WHEN state = 'approved' THEN trans_date END) AS approved_count, 
SUM(amount) AS trans_total_amount, COALESCE(SUM(CASE WHEN state = 'approved' THEN amount END), 0) AS approved_total_amount
FROM Transactions
GROUP BY month, country