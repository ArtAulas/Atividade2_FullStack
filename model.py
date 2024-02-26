from typing import Optional
from pydantic import BaseModel, validator

class Animacao(BaseModel):
    id:Optional[int]=None
    titulo:str
    descricao:str
    episodios: int

    @validator('descricao')
    def validar_descricao(cls, value:str):
        palavras=value.split(" ")
        if len(palavras)<4:
            raise ValueError("A descrição é muito curta. Necessário pelo menos 4 palavras")
        return value
        
    @validator('episodios')
    def validar_episodios(cls, value:int):
        if value==0:
            raise ValueError("Não é possível registrar animações sem episódios")
        return value
        
animacoes=[
    Animacao(id=1, titulo="Bob Esponja",descricao="Desenho Infantil Mais Popular da História",episodios=1234),
    Animacao(id=2, titulo="Dragon Ball",descricao="Anime e Mangá Mais Influente",episodios=575)
]