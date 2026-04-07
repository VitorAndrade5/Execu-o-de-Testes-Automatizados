from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_criar_disciplina():
    payload = {
        "id": 1,
        "titulo": "Python 75",
        "data_inicio": "2026-01-01",
        "data_termino": "2026-06-01",
        "vagas": 50,
        "eh_verao": False
    }
    response = client.post("/disciplinas/", json=payload)
    assert response.status_code == 200


def test_listar_disciplinas():
    response = client.get("/disciplinas/")
    assert response.status_code == 200


def test_deletar_disciplina():
    response = client.delete("/disciplinas/1")
    assert response.status_code == 200