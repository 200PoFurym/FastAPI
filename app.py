from flask import Flask, render_template, request, redirect, url_for

from users.user import user_bp

app = Flask(__name__)

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'fsdfhg4g5g6hfe'

app.register_blueprint(user_bp)

questions = [
    {'id': 1, 'title': 'как использовать Flask?', 'text': 'Я новичок и не знаю как раюотать с Flask'},
    {'id': 2, "title": 'Как скачачть Django?', 'text': 'Я новичок и не знаю как раюотать с Django'}
]

answers = [
    {'id': 1, 'question_id': 1, 'answer': 'Просто скачать Flask через команду pip install flask'},
    {'id': 2, 'question_id': 2, 'answer': 'Просто скачать Flask через команду pip install django'}
]

@app.route('/')
def home():
    return render_template('index.html', questions=questions)

@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((i for i in questions if i['id'] == question_id), None)
    if question:
        question_answer = (a for a in answers if a['question_id'] == question_id)
        return render_template('question.html', question=question, answer=question_answer)
    else:
        return 'Не найдено!!!'

# GET получить данные
# POST отправить данные
# PUT изменить данные
# PATCH изменить определенные данные
# DELETE удаление данных
@app.route('/ask', methods=['POST', 'GET'])
def ask():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        new_question = {
            'id': len(questions) + 1,
            'title': title,
            'text': text
        }
        questions.append(new_question)
        return redirect(url_for('home'))
    else:
        return render_template('ask.html')

@app.route('/slave/<int:title>')
def buy(title):
    return f'<h1>Это продукт {title}</h1>'

app.run(debug=True)