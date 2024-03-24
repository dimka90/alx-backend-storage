-- Task: Create a table named users with specified attributes

-- Create table users with specified attributes
CREATE TABLE IF NOT EXISTS users (
    -- Define id as an integer, auto_increment and a primary key
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -- Define email as a string , never null
    email VARCHAR(255) NOT NULL UNIQUE,
    -- Define name as a string
    name  VARCHAR(255),
    -- Define country as an ENUM type , never NULL with a default value
    country ENUM('US','CO','TN') NOT NULL
);
