CREATE DATABASE IF NOT EXISTS sistema_lavanderia;

-- crear tabla clientes
USE sistema_lavanderia; 
CREATE TABLE IF NOT EXISTS cliente(
    id_cliente varchar(10) not null primary key,
    nombres varchar(20) not null,
    apellidos varchar(20) not null,
    cedula char(10) not null,
    ruc char(13),
    vehiculo varchar(40)
);

CREATE TABLE IF NOT EXISTS turno(
    id_turno varchar(10) not null primary key,
    id_cliente varchar(10) not null,
    tipo_servicio enum("1","2","3"),
    fecha_hora timestamp not null
);