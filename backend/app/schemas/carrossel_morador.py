from pydantic import BaseModel, ConfigDict

class CarrosselMoradorBase(BaseModel):
    url_imagem: str
    ordem_exibicao: int = 0

class CarrosselMoradorCreate(CarrosselMoradorBase):
    id_pessoa: int
    id_imovel: int

class CarrosselMoradorOut(CarrosselMoradorBase):
    id_carrossel_morador: int
    id_pessoa: int
    id_imovel: int

    model_config = ConfigDict(from_attributes=True)
