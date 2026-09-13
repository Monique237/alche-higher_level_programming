-- Create users and grant the required privileges.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON user_0d_2_db.* TO 'user_0d_2'@'localhost';
