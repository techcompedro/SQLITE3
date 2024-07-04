create database mercado;
use mercado;

create table produto (
  id_produto int(11) primary key not null auto_increment,
  nome_produto varchar(25),
  preco_venda_produto float(5),
  preco_compra float(5),
  lucro float(5),
  estoque int(255)
  );
  
SELECT * FROM mercado.produto;
DELETE FROM mercado.produtos WHERE id = 1