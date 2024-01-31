CREATE DATABASE USERS;
USE USERS;

CREATE TABLE user(
   id int not null,
   username varchar(100) not null,
   email varchar(100) not null,
   password varchar(100) not null,
   PRIMARY KEY(id)
);

insert into user(Id,username,email,password)
values(0 , "itay" , "i@walla.com " , "pass");

CREATE TABLE clients(
   name varchar(100) not null,
   email varchar(100) not null,
   phone varchar(30) not null,
   PRIMARY KEY(email)
);

insert into clients(name,email,phone)
values("ita" , "i@walla.com" , "05000000000");

