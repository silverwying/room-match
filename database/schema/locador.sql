CREATE TABLE locador (
  id_locador int PRIMARY KEY
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  cpf_cnpj varchar(18) UNIQUE
);