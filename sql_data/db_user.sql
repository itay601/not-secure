CREATE DATABASE USERS;
USE USERS;

CREATE TABLE user(
   id int not null AUTO_INCREMENT,
   username varchar(100) not null,
   email varchar(100) not null,
   password varchar(100) not null,
   PRIMARY KEY(id), UNIQUE(email)
);

insert into user(Id,username,email,password)
values("itay" , "i@walla.com " , "pass");

CREATE TABLE clients(
   id int not null AUTO_INCREMENT,
   name varchar(100) not null,
   email varchar(100) not null,
   phone varchar(30) not null,
   PRIMARY KEY(id), UNIQUE(email)
);

insert into clients(name,email,phone)
values("ita" , "i@walla.com" , "05000000000");

