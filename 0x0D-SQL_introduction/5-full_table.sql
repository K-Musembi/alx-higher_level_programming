-- print full description of first_table
-- command to use database
USE `hbtn_0c_0`;
-- command to retrieve information from table
SELECT CONCAT('Table ', TABLE_NAME), CONCAT('CREATE TABLE ', TABLE_NAME, ' (') FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'hbtn_0c_0';


