import pytest
from app.trivia import Quiz, Question

# test: respuesta correcta
def test_question_correct_answer():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	assert question.is_correct(0)

# test: respuesta incorrecta
def test_question_incorrect_answer():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	assert not question.is_correct(3)

# test: respuesta fuera de rango (índice)
def test_question_out_of_range_index():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	assert not question.is_correct(4) 

def test_quiz_scoring():
	quiz = Quiz()
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	quiz.add_question(question)

	assert quiz.answer_question(question, 0) == True
	assert quiz.correct_answers == 1