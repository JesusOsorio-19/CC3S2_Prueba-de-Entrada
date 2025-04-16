import pytest
from unittest.mock import patch
from app.trivia import Quiz, Question, run_quiz, get_difficulty_level

# test: respuesta correcta
def test_question_correct_answer():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	assert question.is_correct(0)

# test: respuesta incorrecta
def test_question_incorrect_answer():
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	assert not question.is_correct(3)

# test: respuesta fuera de rango (índice) y manejo de ValueError
@patch('builtins.input', side_effect=['1', '4', '0', 'e'])  # Simulamos una respuesta inválida '4' y luego una válida '0'
@patch('builtins.print')
def test_run_quiz_with_value_error(mock_print, mock_input):
    with pytest.raises(SystemExit):  # Simulamos la salida del juego
        run_quiz()
    mock_print.assert_any_call("Alternativa fuera de rango. Debe ser un numero entre 0-3 o 'e' para finalizar el juego.")  

# test: obtener nivel de dificultad desde input
@patch('builtins.input', side_effect=['2'])
def test_get_difficulty_level(mock_input):
	assert get_difficulty_level() == 2

# test: valores fuera de rango para el nivel de dificultad
@patch('builtins.input', side_effect=['0', '4', '2']) # Simulamos entradas inválidas de niveles(0 y 4), luego una válida
def test_get_difficulty_level_invalid_input(mock_input):
	level = get_difficulty_level()
	assert level == 2 

#test: puntuación correcta en el quiz
def test_quiz_score():	
	quiz = Quiz()
	question = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	quiz.add_question(question)
	quiz.answer_question(question, 0)  # Respuesta correcta
	assert quiz.correct_answers == 1
	

# test: agregar varias preguntas al cuestionario
def test_quiz_add_multiple_questions():
	quiz = Quiz()
	question1 = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
	question2 = Question("¿Quién ganó la Copa del Mundo 2014?", ["Alemania", "Argentina", "Brasil", "Francia"], 0, 2)
	quiz.add_question(question1)
	quiz.add_question(question2)

	assert len(quiz.questions) == 2
	assert quiz.questions[0] == question1
	assert quiz.questions[1] == question2

# test: no hay más preguntas en el cuestionario
def test_get_next_question_returns_none_when_empty():
    quiz = Quiz()
    assert quiz.get_next_question() is None

from unittest.mock import patch

# test: no hay preguntas para el nivel seleccionado
def test_no_questions_for_level():
    quiz = Quiz()

    # Agregar preguntas para nivel 1 y 2, pero no nivel 3
    question1 = Question("¿Qué equipo es el más ganador de la UEFA Champions League?", ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"], 0, 1)
    question2 = Question("¿Quién ganó la Copa del Mundo 2014?", ["Alemania", "Argentina", "Brasil", "Francia"], 0, 2)

    quiz.add_question(question1)
    quiz.add_question(question2)

    # Verifica que no se agreguen preguntas para el nivel 3
    quiz_filtered = [q for q in quiz.questions if q.difficulty == 3]
    assert len(quiz_filtered) == 0  # No debe haber preguntas para el nivel 3

# test: run_quiz se ejecuta como entrada principal
@patch('builtins.input', side_effect=['1', '0', '0', 'e'])  # Simulamos el inicio del juego
def test_run_quiz_execution(mock_input):
    with pytest.raises(SystemExit): # Simulamos la salida del juego
        run_quiz()

# test: ejecución completo del juego con input simulado
@patch('builtins.input', side_effect=['1', '0', '0', 'e'])
@patch('builtins.print')
def test_run_quiz(mock_print, mock_input):
	with pytest.raises(SystemExit): 
		run_quiz()
	mock_print.assert_any_call("Juego finalizado.")

