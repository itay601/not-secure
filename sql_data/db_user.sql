CREATE DATABASE USERS;
USE USERS;

CREATE TABLE user(
   username varchar(100) not null,
   email varchar(100) not null,
   password varchar(100) not null,
   code varchar(100) ,
   UNIQUE(email)
);

insert into user(username,email,password)
values("itay" , "i@walla.com " , "pass");

CREATE TABLE clients(
   name varchar(100) not null,
   email varchar(100) not null,
   phone varchar(30) not null,
   UNIQUE(email), UNIQUE(phone)
);

insert into clients(name,email,phone)
values("ita" , "i@walla.com" , "0500000000");

