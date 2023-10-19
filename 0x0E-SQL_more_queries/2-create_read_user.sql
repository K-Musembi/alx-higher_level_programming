-- create database and user
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user
CREATE USER user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';
-- grant select priviledge
GRANT SELECT
ON hbtn_0d_2
TO user_0d_2@localhost;
