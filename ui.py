from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONTE = "Courier"


class QuizInterface:
	def __init__(self, quiz_brain: QuizBrain):
		self.quiz = quiz_brain
		self.tela = Tk()
		self.centralizar_tela()
		self.tela.title("Quiz")
		self.tela.configure(background=THEME_COLOR, padx=20, pady=20)

		# Label
		self.pontuacao_label = Label(
			text="Pontuação = 0",
			fg="white",
			background=THEME_COLOR,
			font=(FONTE, 15),
			width=40,
			bg="green",
			pady=10
		)
		self.pontuacao_label.grid(row=0, column=0, columnspan=2)

		# Canvas e Text

		self.canvas = Canvas(width=500, height=470, bg="white")
		self.perguntas_label = self.canvas.create_text(
			250,
			235,
			width=490,
			justify="center",
			text="Perguntas que vão aparecer aqui",
			fill="black",
			font=(FONTE, 24),
		)
		self.canvas.grid(row=1, column=0, columnspan=2, pady=10)

		# Buttons
		true_image = PhotoImage(file="./imagens/true.png")
		self.buttons_true = Button(
			image=true_image,
			border=0, bg=THEME_COLOR,
			activebackground=THEME_COLOR,
			command=self.botao_true_pressionado
		)
		self.buttons_true.grid(row=2, column=0)

		false_image = PhotoImage(file="./imagens/false.png")
		self.buttons_false = Button(
			image=false_image,
			border=0, bg=THEME_COLOR,
			activebackground=THEME_COLOR,
			command=self.botao_false_pressionado
		)
		self.buttons_false.grid(row=2, column=1)

		self.pegar_proxima_pergunta()

		self.tela.mainloop()

	def centralizar_tela(self):
		largura_app = 550
		altura_app = 680
		largura_monitor = self.tela.winfo_screenwidth()
		altura_monitor = self.tela.winfo_screenheight()
		x = (largura_monitor / 2) - (largura_app / 2)
		y = (altura_monitor / 2) - (altura_app / 1.8)
		self.tela.geometry(f"{largura_app}x{altura_app}+{int(x)}+{int(y)}")

	def pegar_proxima_pergunta(self):
		self.canvas.configure(bg="white")
		if self.quiz.ainda_tem_perguntas():
			pergunta = self.quiz.proxima_pergunta()
			score = self.quiz.pontuacao
			self.pontuacao_label.configure(text=f"Pontuação = {score}")
			self.canvas.itemconfigure(self.perguntas_label, text=pergunta)
		else:
			self.buttons_true.configure(state="disabled")
			self.buttons_false.configure(state="disabled")

	def botao_true_pressionado(self):
		is_verdadeiro = bool
		if self.quiz.ainda_tem_perguntas():
			questao = self.quiz.lista_de_questoes[self.quiz.numero_da_questao]
			is_verdadeiro = self.quiz.checa_resposta("True", questao.answer)
			self.muda_cor_cartao(is_verdadeiro)
		else:
			self.muda_cor_cartao(is_verdadeiro)
			self.canvas.itemconfigure(self.perguntas_label, text="Você terminou de responder todas as afirmações.")

	def botao_false_pressionado(self):
		is_verdadeiro = bool
		if self.quiz.ainda_tem_perguntas():
			questao = self.quiz.lista_de_questoes[self.quiz.numero_da_questao]
			is_verdadeiro = self.quiz.checa_resposta("False", questao.answer)
			self.muda_cor_cartao(is_verdadeiro)
		else:
			self.muda_cor_cartao(is_verdadeiro)
			self.canvas.itemconfigure(self.perguntas_label, text="Você terminou de responder todas as afirmações.")

	def muda_cor_cartao(self, is_verdadeiro):
		if is_verdadeiro:
			self.canvas.configure(bg="green")
		else:
			self.canvas.configure(bg="red")
		self.tela.after(1000, self.pegar_proxima_pergunta)
