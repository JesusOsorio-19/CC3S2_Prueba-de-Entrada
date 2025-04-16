# Implementamos la clase Question
class Question:

# Inicia una pregunta con descripcion, opciones y respuesta correcta.

    def __init__(self, description, options, correct_answer_idx, difficulty): 

        self.description = description
        self.options = options
        self.correct_answer_idx = correct_answer_idx
        self.difficulty = difficulty

    # Verifica si la respuesta del jugador es correcta.
    def is_correct(self, answer_index):
        return self.correct_answer_idx == answer_index
    
class Quiz:
    def __init__(self):
        self.questions = []                     # Lista para almacenar las preguntas
        self.current_question_index = 0         # Indice de la pregunta actual
        self.correct_answers = 0                    # Contador de respuestas correctas
        self.incorrect_answers = 0                  # Contador de respuestas incorrectas

    def add_question(self, question):
        self.questions.append(question)         # Agrega una pregunta a la lista de preguntas

    def get_next_question(self):
        if self.current_question_index < len(self.questions):                               
            question = self.questions[self.current_question_index]                                                          
            self.current_question_index += 1                        
            return question                     # Devuelve la siguiente pregunta si hay mas preguntas en la lista
        return None
    
    def answer_question(self, question, answer):
        if question.is_correct(answer):          # Verifica si la respuesta es correcta
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1                     
            return False

def get_difficulty_level():
    while True:  # Bucle para repetir la seleccion de nivel si la entrada es invalida
        try:
            level = int(input("Seleccione el nivel de dificultad (1-3): "))  # Pedimos al usuario que seleccione el nivel de dificultad
            if level < 1 or level > 3:  # Verificamos si el nivel es válido
                raise ValueError()
            return level  # Retornamos el nivel seleccionado
        except ValueError:
            print("Nivel de dificultad no valido. Seleccione un nivel entre 1-3.")

def run_quiz():

    print("Bienvenido al juego de Trivia!!!")
    print("Responde las preguntas seleccionando la alternativa correcta.")  

    quiz = Quiz()  # Crea una instancia de la clase Quiz

    level = get_difficulty_level()  # Obtenemos el nivel de dificultad ingresado por del usuario   

    # Agregamos las 10 preguntas al cuestionario, ya cada uno clasificada por nivel de dificultad
    list_questions = [
        Question("Cual es la capital de Bolivia?", ["La Paz", "Oruro", "Sucre", "Santa Cruz"], 2, 3),
        Question("Cual es el oceano mas grande del mundo?", ["Atlantico", "Indico", "Artico", "Pacifico"], 3, 1),
        Question("Quien escribio 'La Ciudad y Los Perros'?", ["Gabriel Garcia Marquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Pablo Neruda"], 1, 2),
        Question("Cual es el continente mas grande?", ["Asia", "Africa", "America", "Europa"], 0, 1),
        Question("Cual es la moneda de Inglaterra?", ["Yen", "Libra Esterlina", "Dolar Ingles", "Euro"], 1, 2),
        Question("Que famoso cientifico formulo la teoria de la relatividad?", ["Issac Newton", "Nikola Tesla", "Albert Einstein", "Stephen Hawking"], 2, 3),
        Question("Que animal tiene el corazon mas grande del mundo?", ["Elefante", "Ballena azul", "Hipopotamo", "Toro"], 1, 2),
        Question("Que elemento quimico tiene el simbolo Au en la tabla periodica?", ["Oro", "Plata", "Cobre", "Aluminio"], 0, 1),
        Question("Que pais tiene forma de bota?", ["Grecia", "Italia", "Espania", "Francia"], 1, 2),
        Question("Quien pinto la Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], 2, 3),
    ]

    filtered_questions = [q for q in list_questions if q.difficulty == level]  # Filtramos las preguntas por nivel de dificultad
    
    for question in filtered_questions:  # Agregamos las preguntas filtradas al cuestionario
        quiz.add_question(question)  

    if not quiz.questions:  # Verificamos si hay preguntas disponibles para el nivel seleccionado
        print("No hay preguntas para el nivel seleccionado.")
        return

    for i in range(len(quiz.questions)):                     # Iteramos 10 veces para hacer 10 preguntas
        question = quiz.get_next_question()
        if question:                                
            print(f"\nPregunta {i + 1}: {question.description}")

            for idx, option in enumerate(question.options):         
                print(f"{idx}. {option}")       # Mostramos las opciones de respuesta desde 0 a 3
        
        while True: #Bucle para repetir la pregunta si la entrada es invalida
            try:
                # Pedimos al usuario que ingrese su respuesta
                user_input = input("Seleccione la alternativa correcta (0-3) o 'e' para finalizar el juego: ")

                if user_input == 'e':  # Si el usuario ingresa 'e', salimos del juego
                    print("Juego finalizado.")
                    print(f"Respuestas correctas: {quiz.correct_answers}")
                    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
                    exit()
                
                user_input = int(user_input)  # Convertimos la entrada en un entero

                # Verificamos si la entrada es un número entre 0 y 3
                if user_input < 0 or user_input >= len(question.options):   
                    raise ValueError()
                
                # Verificamos si la respuesta es correcta
                if quiz.answer_question(question, user_input):
                    print("Respuesta correcta!!!")

                else:
                    print("Respuesta incorrecta. La respuesta correcta era:", question.options[question.correct_answer_idx])

                break  # Salimos del bucle si la respuesta es válida

            except (ValueError, IndexError):
                print("Alternativa fuera de rango. Debe ser un numero entre 0-3 o 'e' para finalizar el juego.")

    print("\nJuego terminado. Aqui tienes tus resultados:")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")

if __name__ == "__main__":
    # Ejecutamos el juego de trivia
    # Esto permite que el juego se ejecute solo si este archivo es el principal
    run_quiz()