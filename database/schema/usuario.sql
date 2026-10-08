CREATE TABLE usuario (
  id_usuario int PRIMARY KEY
    REFERENCES pessoa (id_pessoa) DEFERRABLE INITIALLY IMMEDIATE,
  email varchar(255) UNIQUE NOT NULL,
  senha_hash text NOT NULL,
  telefone varchar(30),
  data_nascimento date,
  foto_perfil text,
  data_cadastro timestamptz NOT NULL,
  bio text,
  cidade_atual varchar(100),
  status_verificacao varchar(30)
);