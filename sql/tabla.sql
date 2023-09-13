CREATE DATABASE IF NOT EXISTS `examen`;

USE `examen`;

CREATE TABLE estudiantes (
    id INT PRIMARY KEY,
    nombre VARCHAR(150),
    apellido VARCHAR(150),
    edad VARCHAR(50),
    fecha_registro date()
);
