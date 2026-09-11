from pydantic import BaseModel, ConfigDict


class CarrosselImagemBase(BaseModel):
    url_imagem: str
    ordem_exibicao: int = 0


class CarrosselImagemCreate(CarrosselImagemBase):
    id_imovel: int


class CarrosselImagemOut(CarrosselImagemBase):
    id_imagem: int
    id_imovel: int

    model_config = ConfigDict(from_attributes=True)
