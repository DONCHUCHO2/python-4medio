create database sqltrasporte1; #acá se crea la base de datos
show databases; #pedimos que nos muestre todas las 
use sqltrasporte1;

create table vehiculo(
id int auto_increment,
marca char(45) not null,
color char(45) not null,
primary key (id)
);

insert into vehiculo (marca, color) values
    ('honda', 'azul'),
    ('toyota','rojo'),
    ('chevrolet','morado');
    
    
create table taxi(
id int auto_increment,
marca char(45) not null,
color char(45) not null,
el_auto_de int not null,
primary key (id),
foreign key(el_auto_de) references vehiculo(id)
); 

insert into taxi (marca, color, el_auto_de) values
    ('mitsubishi', 'verde','1'),
    ('bmw','blanco','2'),
    ('fordt','negro','3');

create table micro(
id int,
marca char(45) not null,
color char(45) not null,
el_dueño_es int not null,
primary key (id),
foreign key(el_dueño_es) references vehiculo(id)
);

alter table micro modify column id int auto_increment;

insert into micro (marca, color, el_dueño_es) values
    ('merzedes', 'marron','2'),
    ('hiunday','plomo','3'),
    ('suzuki','cafe','1');