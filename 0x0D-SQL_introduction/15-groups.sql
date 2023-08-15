-- Count records with the same score in second_table
SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;
