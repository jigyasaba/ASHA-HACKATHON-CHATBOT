from flask import Flask, render_template, request, session, redirect, url_for
from questions import questions

app = Flask(__name__)
app.secret_key = 'asha-secret-key'  # For session tracking


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'step' not in session:
        session['step'] = 0
        session['answers'] = []

    if request.method == 'POST':
        user_response = request.form['message']
        session['answers'].append(user_response)
        session['step'] += 1

    step = session['step']
    if step < len(questions):
        question = questions[step]
    else:
        question = "Thank you for sharing, lil sis 💖 Asha is proud of you!"

    return render_template('index.html', question=question, step=step, answers=session['answers'], questions=questions)


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
