from locust import HttpUser, task

class TriviaUser(HttpUser):
    @task
    def get_home(self):
        self.client.get("/")

    @task
    def post_question(self):
        self.client.post("/questions/", json={
            "description": "¿Qué equipo es el más ganador de la UEFA Champions League?",
            "options": ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"],
            "correct_answer": 0
        })
