from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask' 
db = SQLAlchemy(app)


class Flask(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    number = db.Column(db.String(120), nullable=False)
    DateTime = db.Column(db.String(120), nullable=True)


@app.route('/', methods=['GET' ,'POST'])
def hello_world():
    if(request.method=='POST'):
        name = request.form.get('name')
        address = request.form.get('address')
        number = request.form.get('number')

        entry = Flask(name=name, address=address, number=number, DateTime=datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

if __name__==("__main__"):
    app.run(debug=True)
 