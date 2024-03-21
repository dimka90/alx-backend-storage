-- An Sql script that creates a table users following these requirements

-- Create table users with specified attributes
CREATE TABLE   IF NOT EXISTS users (
-- Define id as an integer, auto increment, and primary key
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
-- Define email as a string of 255 characters, never null, and unique
email VARCHAR(255) NOT NULL UNIQUE,
-- Define name as a string of 255 characters
name VARCHAR(255)
);
