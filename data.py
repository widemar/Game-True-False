import requests

question_data = []

resposta = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
resposta.raise_for_status()
dados_api = resposta.json()

for item in dados_api["results"]:
	question_data.append(
		{
			"question": item["question"],
			"correct_answer": item["correct_answer"]
		}
	)
