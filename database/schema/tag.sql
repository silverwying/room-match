CREATE TABLE tag (
  id_tag SERIAL PRIMARY KEY,
  nome varchar(100) UNIQUE NOT NULL,
  categoria varchar(50)
);