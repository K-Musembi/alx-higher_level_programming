-- create database and table
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use databse
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities (
	`id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`state_id` INT NOT NULL FOREIGN KEY (id) REFERENCES (states),
	`name` VARCHAR(256) NOT NULL,
	UNIQUE (id)
);	
