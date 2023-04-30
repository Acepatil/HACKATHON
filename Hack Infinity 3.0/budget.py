from re import template
import sqlalchemy as sqlalchemy
from datetime import datetime
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
local_server = True
local_server2 = True

with open('config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']


with open('config2.json','r') as c:
    params = json.load(c)["params2"]
if(local_server2):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri2']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri2']

db = SQLAlchemy(app)

class Budget_Manager(db.Model):
    '''
    Serial_num,Name,age,income,expenses,occupation,taxes,age,loan
    '''
    Name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    mobile_number = db.Column(db.String(50), unique=True, nullable=False)

class Monthly(db.Model):
    '''
    Serial_num,Name,age,income,expenses,occupation,taxes,age,loan
    '''
    Occupation = db.Column(db.String(50), unique=False, nullable=False)
    income = db.Column(db.String(50), unique=False, nullable=False)
    taxes = db.Column(db.String(50), unique=False, nullable=False)

@app.route("/")
def budget():
    return render_template('Front.html')
@app.route("/monthly",methods = ['GET','POST'])
def Monthly():
    if (request.method == 'POST'):
        occupation = request.form.get('occupation')
        income = request.form.get('income')
        taxes = request.form.get('taxes')
        entry = Budget_Manager(occupation='occupation', income='income', taxes='taxes')
        db.session.add(entry)
        db.session.commit()
    return render_template('Monthly.html')
@app.route("/contact", methods = ['GET','POST'])
def contact():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('mobile_number')
        entry = Budget_Manager(name=name, phone_num=phone_number, email=email)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


@app.route("/page")
def page():
    return render_template('page.html')

app.run(debug=True)