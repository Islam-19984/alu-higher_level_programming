-- Script that create an user and a database in MYSQL server
-- Query to create the user 'user_0d_1' and the database 'hbtn_0d_2' in MYSQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2.* To 'user_0d_2'@'localhost';
