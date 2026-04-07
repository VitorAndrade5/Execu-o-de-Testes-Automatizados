from behave import Given, When, Then
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@Given('que o sistema está iniciado')
def step_impl(context):
    context.res = client.get("/disciplinas/")
    assert context.res.status_code == 200

@When('eu cadastro uma disciplina com título "{titulo}" e {vagas:d} vagas')
def step_impl(context, titulo, vagas):
    data = {
        "id": 1,
        "titulo": titulo,
        "data_inicio": "2026-01-01",
        "data_termino": "2026-06-01",
        "vagas": vagas,
        "eh_verao": False
    }
    context.res = client.post("/disciplinas/", json=data)

@Then('a disciplina deve aparecer na lista com sucesso')
def step_impl(context):
    assert context.res.status_code == 200
    assert context.res.json()["dados"]["titulo"] == "Python Básico"