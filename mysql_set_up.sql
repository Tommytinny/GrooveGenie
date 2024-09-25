-- creates the MySQL server Database hbnb_dev_db and user hbnb_dev
-- Grant privileges om database

CREATE DATABASE IF NOT EXISTS groovie_db;
CREATE USER IF NOT EXISTS 'admin'@'localhost'
IDENTIFIED BY 'Wakeup_11!';
GRANT ALL PRIVILEGES ON groovie_db.* To 'admin'@'localhost';
GRANT SELECT ON performance_schema.* TO 'admin'@'localhost';
