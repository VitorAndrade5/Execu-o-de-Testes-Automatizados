from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import List

app = FastAPI()

class Disciplina(BaseModel):
    id: int
    titulo: str
    data_inicio: date
    data_termino: date
    vagas: int
    eh_verao: bool

db: List[Disciplina] = []

@app.post("/disciplinas/")
def criar_disciplina(disciplina: Disciplina):
    db.append(disciplina)
    return {"mensagem": "Disciplina criada!", "dados": disciplina}

@app.get("/disciplinas/")
def listar_disciplinas():
    return db

@app.put("/disciplinas/{id_disciplina}")
def atualizar_disciplina(id_disciplina: int, disciplina_atualizada: Disciplina):
    for index, d in enumerate(db):
        if d.id == id_disciplina:
            db[index] = disciplina_atualizada
            return {"mensagem": "Atualizado com sucesso"}
    raise HTTPException(status_code=404, detail="Disciplina não encontrada")

@app.delete("/disciplinas/{id_disciplina}")
def deletar_disciplina(id_disciplina: int):
    for index, d in enumerate(db):
        if d.id == id_disciplina:
            db.pop(index)
            return {"mensagem": "Removido com sucesso"}
    raise HTTPException(status_code=404, detail="Não encontrada")