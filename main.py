from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from time import sleep
from model import Animacao
from model import animacoes


def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)

app = FastAPI(
    title='API de Animações',
    version='0.0.2',
    description='Uma API Fast'
)

@app.get('/animacoes',
         description='Retorna todas as animações cadastradas.',
         summary='Retorna as animações',
         response_model=List[Animacao],
         response_description='Animações encontrados com sucesso.')
async def get_animacoes(db: Any = Depends(fake_db)):
    return animacoes

@app.post('/animacoes', status_code=status.HTTP_201_CREATED, response_model=Animacao)
async def post_animacao(animacao: Animacao):
    next_id: int = len(animacoes) + 1
    animacao.id = next_id
    animacoes.append(animacao)
    return animacao

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
