from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

banco_de_perguntas = []

for questao in question_data:
	text = questao["question"]
	answer = questao["correct_answer"]
	nova_pergunta = Question(text, answer)
	banco_de_perguntas.append(nova_pergunta)

quiz = QuizBrain(banco_de_perguntas)
tela = QuizInterface(quiz)

