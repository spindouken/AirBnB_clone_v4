-- Prepare MySQL server for the project
DROP DATABASE IF EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Create tables
CREATE TABLE states (
    id VARCHAR(60) PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE cities (
    id VARCHAR(60) PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
);

CREATE TABLE users (
    id VARCHAR(60) PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128)
);

CREATE TABLE places (
    id VARCHAR(60) PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description VARCHAR(1024),
    number_rooms INT NOT NULL DEFAULT 0,
    number_bathrooms INT NOT NULL DEFAULT 0,
    max_guest INT NOT NULL DEFAULT 0,
    price_by_night INT NOT NULL DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    FOREIGN KEY (city_id) REFERENCES cities (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE amenities (
    id VARCHAR(60) PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE reviews (
    id VARCHAR(60) PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    place_id VARCHAR(60) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    text VARCHAR(1024) NOT NULL,
    FOREIGN KEY (place_id) REFERENCES places (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE place_amenity (
    place_id VARCHAR(60),
    amenity_id VARCHAR(60),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places (id),
    FOREIGN KEY (amenity_id) REFERENCES amenities (id)
);
