from flask import Flask, render_template, request, send_file, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:uriel@localhost/mine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class datafiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200), unique=True)

    def __init__(self, data):
        self.data = data


@app.route('/')
def index():
    return render_template('new.html')

@app.route('/page', methods= ['GET', 'POST'])
def page():
    if request.method == 'POST':
        file = request.files['form']

        file.save(f'uploads/{file.filename}')




        data = datafiles(data=f'{secure_filename(file.filename)}')
        db.session.add(data)
        db.session.commit()

    return render_template('page.html',input = file.filename)


if __name__ == "__main__":

    app.run(debug = True)

