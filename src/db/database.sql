DROP DATABASE IF EXISTS examen_final;
CREATE DATABASE examen_final;
USE examen_final;

CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    password VARCHAR(255)
);

CREATE TABLE contacts (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(50),
    phone VARCHAR(50),
    email VARCHAR(150),
    user_id INT UNSIGNED,

    FOREIGN KEY (user_id) REFERENCES users(id)
)