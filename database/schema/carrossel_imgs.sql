CREATE TABLE carrossel_imgs (
  id_imagem BIGSERIAL PRIMARY KEY,
  id_imovel int NOT NULL
    REFERENCES imovel (id_imovel) DEFERRABLE INITIALLY IMMEDIATE,
  url_imagem text NOT NULL,
  ordem_exibicao int NOT NULL
);

CREATE UNIQUE INDEX ON carrossel_imgs (id_imovel, ordem_exibicao);
