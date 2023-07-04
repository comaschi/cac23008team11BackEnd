create database if not EXISTS cac23008team11;

use cac23008team11;


;
-- drop table pedidos
;

create table
    pedidos (
        uuId varchar(36) not null,
        platoId int not null,
        cantidad decimal(10, 2),
        time timestamp,
        index (uuid)
    );

create table
    platos (
        platoId int not null AUTO_INCREMENT,
        title varchar(255),
        description varchar(255),
        imageUrl varchar(255),
        precio decimal(8, 2),
        primary key(platoId)
    );

insert into
    platos (
        title,
        imageUrl,
        description,
        precio
    )
values
    row(
        'Cordero Patagonico',
        'http://www.skorpios.cl/wp-content/uploads/El-cordero-patag%C3%B3nico-de-Skorpios.jpg',
        'plato típico de la región patagónica de Argentina que se prepara al asador y se sirve con guarniciones como papas y ensalada.',
        7000
    ),
    row(
        'Bife de Costilla',
        'https://www.lamejorparrilla.com/wp-content/uploads/2011/02/1470069566_1461178446bife-de-costilla.png',
        'Exquisito Bife de Costilla, asado a las brazas con Papas al natutal como guarnicion',
        4500
    ),
    row (
        'Bife estilo Campo',
        'https://www.lamejorparrilla.com/wp-content/uploads/2011/02/1470069659_1461178373bife-estilo-campo.png',
        'corte de carne de res que se cocina a la parrilla y se sazona con especias y hierbas frescas.',
        5000
    ),
    ROW (
        'Achuras',
        'https://www.lamejorparrilla.com/wp-content/uploads/2011/02/1470069637_1461178564achuras.png',
        'Fina seleccion de las mejores achuras, mollejas chinchulines, riñones y morcillas',
        3500
    ),
    ROW (
        'Entraña',
        'https://www.lamejorparrilla.com/wp-content/uploads/2017/11/don-julio-6.jpg',
        'Exquisita carne que se despega del costillar del asado. Es muy sabrosa y tierna, por lo general  se prefiere en entradas pero también va excelente como plato principal',
        5000
    ),
    ROW (
        'Brochette de lomo',
        'https://i1.wp.com/lacabrera.com.ar/wp-content/uploads/2015/09/brochette-de-lomo-cebolla-y-panceta.jpg',
        'Un sabor delicioso y una buena opción para comer carne y vegetales.',
        5000
    ),
    ROW (
        'Chivito',
        'https://www.lamejorparrilla.com/wp-content/uploads/2011/02/1470069323_1461178513chivito.png',
        'Prueba el mejor cabrio asado por expertos',
        6500
    ),
    ROW (
        'Tabla de Chorizos',
        'https://www.lamejorparrilla.com/wp-content/uploads/2017/11/don-julio-3.jpg',
        'Deléitate con nuestra variedad de chorizos asados a la perfección. Acompañados de salsa, pan y opción de ensalada o papas fritas. ¡Una experiencia parrillera única!',
        6500
    ),
    ROW (
        'Provoleta',
        'https://i1.wp.com/lacabrera.com.ar/wp-content/uploads/2015/09/PROVOLETA.jpg',
        'Sale antes o durante el asado, según los tiempos del parrillero. Es muy común que se la condimente con especias que le dan un excelente aroma y la convierten en tentadoras para cualquier comensal.',
        3500
    ),
    ROW (
        'Empanadas',
        'https://i1.wp.com/lacabrera.com.ar/wp-content/uploads/2010/01/LC_Web_Headers_sept-04.jpg',
        'Sabrosas y calentitas, no te las podés perder. Son una excelente elección como entrada para que abra el apetito mientras esperamos lo que viene.',
        3500
    ),
    ROW (
        'Ensaladas varias',
        'https://i1.wp.com/lacabrera.com.ar/wp-content/uploads/2015/09/ensalada-varias.jpg',
        'Para acompañar los platos que más te gustan te damos la oportunidad de combinarlas con tus verduras y gustos preferidos.',
        2500
    ),
    ROW (
        'Verduras Asadas',
        'https://www.lamejorparrilla.com/wp-content/uploads/2017/11/don-julio-5.jpg',
        'Seleccion de las mejores Verduras de estacion asadas a su mejor punto. un deleite',
        2500
    )

;

select