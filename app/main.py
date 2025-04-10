from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Trivia Game API is running!"}