from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class LivroEntrada(BaseModel):
    titulo: str
    autor: str
    ano: int


class Livro(LivroEntrada):
    id: int


app = FastAPI()
livros: dict[int, Livro] = {}
proximo_id = 1


@app.get("/health")
def verificar_saude():
    return {"status": "ok"}


@app.get("/livros")
def listar_livros() -> list[Livro]:
    return list(livros.values())


@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int) -> Livro:
    if livro_id not in livros:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livros[livro_id]


@app.post("/livros", status_code=201)
def criar_livro(livro: LivroEntrada) -> Livro:
    global proximo_id
    livro_criado = Livro(id=proximo_id, **livro.model_dump())
    livros[proximo_id] = livro_criado
    proximo_id += 1
    return livro_criado


@app.put("/livros/{livro_id}")
def atualizar_livro(livro_id: int, dados: LivroEntrada) -> Livro:
    if livro_id not in livros:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    livro_atualizado = Livro(id=livro_id, **dados.model_dump())
    livros[livro_id] = livro_atualizado
    return livro_atualizado


@app.delete("/livros/{livro_id}")
def remover_livro(livro_id: int):
    if livro_id not in livros:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    del livros[livro_id]
    return {"mensagem": "Livro removido"}