-- create database and table
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	UNIQUE (id)
);
