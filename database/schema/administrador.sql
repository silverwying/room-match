CREATE TABLE administrador (
  id_administrador int PRIMARY KEY
    REFERENCES usuario (id_usuario) DEFERRABLE INITIALLY IMMEDIATE,
  nivel_acesso varchar(30) NOT NULL,
  data_admissao date NOT NULL
);