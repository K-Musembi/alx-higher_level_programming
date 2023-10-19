-- list cities of California
-- use database
USE hbtn_0d_usa;
-- select cities
SELECT *
FROM cities
WHERE state_id in (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
