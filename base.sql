drop database metrica_AB;
create database metrica_AB;
use metrica_AB;
show tables;
drop table usuario; 
select * from usuario;
SELECT
	COUNT(0) total,
    SUM(colocou_email) quantos_colocaram_email,
    SUM(comprou) quantos_compraram,
    ROUND(SUM(comprou)/COUNT(0)*100,2) taxa_conversao
FROM usuario where usuario.teste = 'A';

SELECT
	COUNT(0) total,
    SUM(colocou_email) quantos_colocaram_email,
    SUM(comprou) quantos_compraram,
    ROUND(SUM(comprou)/COUNT(0)*100,2) taxa_conversao
FROM usuario where usuario.teste = 'B';
