FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./users_clients.sql /docker-entrypoint-initdb.d/

EXPOSE 80
