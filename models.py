from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), unique=True)
    start_time = db.Column(db.DateTime, default=db.func.now())
    completed = db.Column(db.Boolean, default=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_number = db.Column(db.Integer)
    question_text = db.Column(db.String(500))
    answer_text = db.Column(db.String(500))
