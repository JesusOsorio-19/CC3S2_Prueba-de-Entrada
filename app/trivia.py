# Implementamos la clase Question
class Question:

# Inicia una pregunta con descripción, opciones y respuesta correcta.

    def __init__(self, description, options, correct_answer_idx): 

        self.description = description
        self.options = options
        self.correct_answer_idx = correct_answer_idx

# Verifica si la respuesta del jugador es correcta.

    def is_correct(self, answer_index):
        return self.correct_answer_idx == answer_index