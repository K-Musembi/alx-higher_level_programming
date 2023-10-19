-- list cities in database
-- command to use database
USE hbtn_0d_usa
-- command to select cities
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities
JOIN hbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id;
