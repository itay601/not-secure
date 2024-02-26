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
values("Me" , "itaymerel1212@gmail.com" , "$argon2id$v=19$m=65536,t=3,p=4$IqKQwvcAjh7PezWlDpExhA$VeuX1EAVjkIx+dGK/qeCynjPfc1nqY+fi6jo2Ap8UPg");


CREATE TABLE clients(
   name varchar(100) not null,
   email varchar(100) not null,
   phone varchar(30) not null,
   PRIMARY KEY(email), UNIQUE(email), UNIQUE(phone)
);

insert into clients(name,email,phone)
values("ita" , "i@walla.com" , "0500000000");

CREATE TABLE userpass(
   id int not null AUTO_INCREMENT,
   uname varchar(100) not null,
   passwordtemp varchar(100) not null,
   passwordsecond varchar(100) not null,
   passwordthird varchar(100) not null, 
   PRIMARY KEY(id), FOREIGN KEY(uname) REFERENCES user(username)
);

insert into userpass(uname, passwordtemp, passwordsecond, passwordthird)
values("Me","-","-","-");
