CREATE DATABASE user;
USE user;


CREATE TABLE IF NOT EXISTS users (
	id int not null PRIMARY KEY,
	username varchar(100) NOT NULL,
	mail varchar(100) NOT NULL,
	password TEXT NOT NULL,
);

CREATE INDEX IF NOT EXISTS users_name_idx ON users (name);

insert into users(id,username,mail,password)
VALUES("123456789",itay601,itay@gmail.com,12345678);
