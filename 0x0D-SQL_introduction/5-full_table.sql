-- print full description of first_table
-- command to use database
USE `hbtn_0c_0`;
-- command to retrieve information from table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA, COLUMN_COMMENT
FROM information_schema.columns
WHERE TABLE_SCHEMA = "hbtn_0c_0" AND TABLE_NAME = "first_table";

