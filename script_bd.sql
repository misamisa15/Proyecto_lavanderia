DROP DATABASE sistema_lavanderia;
CREATE DATABASE IF NOT EXISTS sistema_lavanderia;

-- crear tabla clientes
USE sistema_lavanderia; 
CREATE TABLE IF NOT EXISTS cliente(
    id_cliente char(10) not null primary key,
    nombres varchar(20) not null,
    apellidos varchar(20) not null,
    cedula char(10) not null,
    ruc char(13),
    vehiculo varchar(40)
);

CREATE TABLE IF NOT EXISTS turno(
    id_turno char(10) not null primary key,
    id_cliente char(10) not null,
    tipo_servicio enum("1","2","3"),
    fecha_hora timestamp not null
);

alter table turno add constraint fk_turn_cliente foreign key (id_cliente) references cliente(id_cliente) on delete cascade on update cascade; 


CREATE TABLE IF NOT EXISTS comprobante(
    id_comprobante char(10) not null primary key,
    id_turno char(10) not null,
    fecha_hora timestamp not null
);
alter table comprobante add constraint fk_comprobante_turno foreign key (id_turno) references turno(id_turno) on delete cascade on update cascade;

CREATE TABLE IF NOT EXISTS cuenta_por_cobrar(
    id_cuenta_cobrar char(10) not null primary key,
    id_cliente char(10) not null,
    id_turno char(10) not null,
    fecha_hora timestamp not null,
    total double not null
);
alter table cuenta_por_cobrar add constraint fk_cuentaC_cliente foreign key (id_cliente) references cliente(id_cliente) on delete cascade on update cascade; 
alter table cuenta_por_cobrar add constraint fk_cuentaC_turno foreign key (id_turno) references turno(id_turno) on delete cascade on update cascade;



CREATE TABLE IF NOT EXISTS factura_cliente(
    id_factura char(10) not null primary key,
    id_cliente char(10) not null,
    id_turno char(10) not null,
    fecha_hora timestamp not null,
    total double not null
);
alter table factura_cliente add constraint fk_factura_cliente foreign key(id_cliente) references cliente(id_cliente) on delete cascade on update cascade; 
alter table factura_cliente add constraint fk_factura_turno foreign key (id_turno) references turno(id_turno) on delete cascade on update cascade;


 CREATE TABLE IF NOT EXISTS producto(
    id_producto_inv char(10) not null primary key,
    nombre varchar(30) not null,
    descripcion varchar(50) not null,
    stock int not null,
    precio double not null
 );

CREATE TABLE IF NOT EXISTS factura_producto(
    id_factura_producto char(10) not null primary key,
    id_factura char(10) not null,
    id_producto char(10) not null,
    cantidad int not null
 );

 alter table factura_producto add constraint fk_producto_factura foreign key (id_factura) references factura_cliente(id_factura) on delete cascade on update cascade;
 alter table factura_producto add constraint fk_facPro_Producto foreign key (id_producto) references producto(id_producto_inv) on delete cascade on update cascade;


CREATE TABLE IF NOT EXISTS trabajador(
    id_trabajador char(10) not null primary key,
    nombres varchar(20) not null,
    apellidos varchar(20) not null,
    cedula char(10) not null,
    contrato enum("1","2","3"),
    fecha_contrato timestamp not null,
    salario double not null
);

CREATE TABLE IF NOT EXISTS administrador(
    id_admin char(10) not null primary key,
    id_trabajador char(10) not null,
    clave varchar(16) not null
 );

 alter table administrador add constraint fk_administrador_trabajador foreign key (id_trabajador) references trabajador(id_trabajador) on delete cascade on update cascade;

CREATE TABLE IF NOT EXISTS pedido(
    id_pedido char(10) not null primary key,
    descripcion varchar(50) not null,
    total  double not null
);

CREATE TABLE IF NOT EXISTS proveedor(
    id_proveedor char(10) not null primary key,
    nombres varchar(20) not null,
    apellidos varchar(20) not null,
    ruc char(13) not null,
    empresa varchar(20) not null
);

CREATE TABLE IF NOT EXISTS factura_proveedor(
    id_fac_prov char(10) not null primary key,
    id_proveedor char(10) not null,
    id_pedido char(10)  not null,
    id_admin char(10) not null,
    codigo_factura char(20) not null,
    total double not null
);

alter table factura_proveedor add constraint fk_facprov_pedido foreign key (id_pedido) references  pedido(id_pedido) on delete cascade on update cascade;
alter table factura_proveedor add constraint fk_facprov_admin foreign key (id_admin) references  administrador(id_admin) on delete cascade on update cascade;
alter table factura_proveedor add constraint fk_facprov_proveedor foreign key (id_proveedor) references proveedor(id_proveedor)  on delete cascade on update cascade;