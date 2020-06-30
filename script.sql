USING mqsql;
DROP DATABASE IF EXISTS recipedb;
CREATE DATABASE recipedb
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
CREATE USER 'django-user'@'localhost' IDENTIFIED BY 'django-user-password';
GRANT ALL PRIVILEGES ON * . * TO 'django-user'@'localhost';
FLUSH PRIVILEGES
