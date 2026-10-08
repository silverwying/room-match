CREATE TABLE endereco_imovel (
  id_endereco SERIAL PRIMARY KEY,
  id_imovel int UNIQUE NOT NULL
    REFERENCES imovel (id_imovel) DEFERRABLE INITIALLY IMMEDIATE,
  rua varchar(255) NOT NULL,
  numero varchar(20) NOT NULL,
  complemento varchar(100),
  bairro varchar(100),
  cidade varchar(100),
  estado varchar(100),
  cep varchar(20),
  latitude decimal(10,7),
  longitude decimal(10,7)
);