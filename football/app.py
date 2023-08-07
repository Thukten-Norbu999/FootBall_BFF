from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
import hashlib
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)




class Matches(db.Model):
    id = db.Column(db.String, primary_key=True, unique=True, default=lambda:str(uuid.uuid4()))
    homeTeam = db.Column(db.String(100), nullable=False)
    awayTeam = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(10000), nullable=False)
    id_code = f'{homeTeam} vs {awayTeam} - {category}'.encode('utf-8')
    identifier = db.Column(db.String(10000), unique=True)
    matchDate = db.Column(db.Date, nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.homeTeam} vs {self.awayTeam} - {self.category}'


def create_database():
    if not os.path.exists('database.db'):
        with app.app_context():
            db.create_all()
create_database()



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/matches')
def viewMatch():
    matches = Matches.query.all()
    return render_template('viewMatch.html', matches=matches)


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        homeTeam = request.form.get('homeTeam').lower()
        awayTeam = request.form.get('awayTeam').lower()
        matchDate = request.form.get('matchDate').split('-')
        category = request.form.get('category')
        id_code = f'{homeTeam} vs {awayTeam}'.encode('utf-8')
        idf = hashlib.sha256(id_code).hexdigest()

        if not Matches.query.filter_by(identifier=idf).first():
            new_match = Matches(
                homeTeam=homeTeam,
                awayTeam=awayTeam,
                matchDate=datetime.date(
                    int(matchDate[0]),
                    int(matchDate[1]),
                    int(matchDate[2])
                ),
                category=category
            )
            db.session.add(new_match)
            db.session.commit()
        else:
            return '<h1>match exists</h1>'
    return render_template('enter.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
