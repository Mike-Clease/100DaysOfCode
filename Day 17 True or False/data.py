import requests
import html

url = "https://opentdb.com/api.php?amount=12"
"&category=9&difficulty=medium&type=boolean"

request = requests.get(url)

data = request.json()['results']

question_data = []
for i in data:
    pair = {}
    text = html.unescape(i['question'])
    answer = i['correct_answer']
    pair['text'] = text
    pair['answer'] = answer
    question_data.append(pair)

for i in question_data:
    print(i['text'])
