import pytest
from app.trivia import Question

# test: respuesta correcta
def test_question_correct_answer():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0)
	assert question.is_correct(0)

# test: respuesta incorrecta
def test_question_incorrect_answer():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0)
	assert not question.is_correct(3)

# test: respuesta fuera de rango (índice)
def test_question_out_of_range_index():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0)
	assert not question.is_correct(4) 