-- List records with score >= 10 from second_table ordered by score
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
