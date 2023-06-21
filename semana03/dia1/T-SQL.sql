#Visualizar una base datos
SHOW DATABASES;

#Hola soy un comentario
CREATE DATABASE codigo;

#Crear una tabla
CREATE TABLE alumnos(
	id int,
    nombre varchar(255),
    apellido varchar(255)
);

#seleccionar tabla
SELECT * FROM alumnos;

#Insertar datos en uan tabla
INSERT INTO alumnos(id,nombre,apellido)values(2,'Cesar','Mayta'),
(3,'Jesus','Chiroque'),(4,'Javier','Zumaran'),(5,'Luis','Carrillo'),(6,'Pedro','Enriquez'),(7,'Jorge','Dueñas'),
(8,'Lionel','Messi'),(9,'Cristiano','Ronaldo'),(10,'Neymar','Jr');

#Consultar algunas columnas de un tabla
SELECT id,nombre FROM alumnos;

#Sentencia Where
SELECT id, nombre FROM alumnos where id < 6;

# Operadores AND,OR, NOT
SELECT * FROM alumnos WHERE id<8 AND ID >3;

#Order by
SELECT * from ALUMNOS order by nombre Desc;
SELECT * from ALUMNOS order by nombre Desc,nombre ASC;

#Update
SET SQL_SAFE_UPDATEs=0;
UPDATE alumnos
set nombre = 'Alfred', apellido='Sanchez' where id=4;

SET SQL_SAFE_UPDATES=1;

# Delete
SET SQL_SAFE_UPDATEs=0;
DELETE FROM alumnos WHERE id=10;
SET SQL_SAFE_UPDATEs=1;

#Like
SELECT * FROM alumnos;
SELECT * FROM alumnos Where nombre Like 'c%';
SELECT * FROM alumnos Where nombre Like '%o';
SELECT * FROM alumnos Where nombre Like '%e%';
SELECT * FROM alumnos Where nombre Like '_e%';
SELECT * FROM alumnos Where nombre Like '__O%';
SELECT * FROM alumnos Where id regexp '[0-5]';

