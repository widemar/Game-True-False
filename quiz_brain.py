import html
from deep_translator import GoogleTranslator


class QuizBrain:
	def __init__(self, lista_de_questoes):
		self.numero_da_questao = 0
		self.lista_de_questoes = lista_de_questoes
		self.pontuacao = 0

	def proxima_pergunta(self):
		questao = self.lista_de_questoes[self.numero_da_questao]
		self.numero_da_questao += 1
		questao_unescape = html.unescape(questao.text)
		questao_traduzida = GoogleTranslator(source="auto", target="pt").translate(questao_unescape)
		return f"Q.{self.numero_da_questao}: {questao_traduzida}"

	def ainda_tem_perguntas(self):
		if self.numero_da_questao < len(self.lista_de_questoes):
			return True
		else:
			return False

	def checa_resposta(self, resposta_usuario, resposta_correta):
		if resposta_usuario.lower() == resposta_correta.lower():
			self.pontuacao += 1
			return True
		else:
			return False
