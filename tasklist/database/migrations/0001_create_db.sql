USE tasklist;

SET foreign_key_checks = 0;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    uuid BINARY(16) PRIMARY KEY,
    name NVARCHAR(32)
);

DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    uuid BINARY(16) PRIMARY KEY,
    description NVARCHAR(1024),
    completed BOOLEAN,
    user_uuid BINARY(16), 
    FOREIGN KEY (user_uuid) REFERENCES users(uuid)
    
);

SET foreign_key_checks = 1;