from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_question(): 
    # Verifica que la API esté en funcionamiento
    response = client.post("/questions/", json={
        "description": "¿Qué equipo es el más ganador de la UEFA Champions League?",
        "options": ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"],
        "correct_answer": 0
    })
    assert response.status_code == 201 # Verifica que la respuesta sea 201 (Creado)
    # Verifica que la respuesta contenga los datos correctos
    assert response.json()["description"] == "¿Qué equipo es el más ganador de la UEFA Champions League?"                       
    assert response.json()["options"][0] == "Real Madrid"               
