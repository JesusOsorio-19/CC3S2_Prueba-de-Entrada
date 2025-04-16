from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.config import DATABASE_URL, SECRET_KEY

print("DATABASE_URL cargada:", DATABASE_URL)
print("SECRET_KEY cargada:", SECRET_KEY)

app = FastAPI()

class QuestionCreate(BaseModel):
    description: str
    options: List[str]
    correct_answer: int

@app.get("/")
def read_root():
    return {"message": "Trivia Game API is running!"}

@app.post("/questions/", status_code=201)       
def create_question(question: QuestionCreate):
    # En una versión completa esto se guardaría en la base de datos
    return question
