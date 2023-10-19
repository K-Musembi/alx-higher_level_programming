-- list top records
-- command to use database
USE hbtn_0c_0;
-- command to show top records
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
