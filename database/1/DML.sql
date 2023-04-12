CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT * FROM users;

SELECT first_name, age FROM users;

drop TABLE users;

SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;

SELECT DISTINCT country FROM users;

SELECT DISTINCT first_name, country FROM users ORDER BY country;

SELECT first_name, balance, age FROM users
WHERE age >= 30 AND balance >= 500000;

SELECT first_name, balance, age FROM users
WHERE first_name LIKE '%호%';

SELECT first_name, balance, age FROM users
ORDER BY age LIMIT 10;

SELECT first_name, balance, age FROM users
ORDER BY age LIMIT 10 OFFSET 5;
