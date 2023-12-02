from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
import pickle
import os

users = []

app = Flask('lab09')
app.config.from_object('config')

if os.path.isfile('data.pickle'):
    with open('data.pickle', 'rb') as file:
        users = pickle.load(file)
else:
    users = []

@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    for user in users:
        if user[0] == login:
            if user[2] == password:
                return redirect(url_for('page3'))
            else:
                return "Wrong password", 401
    return "Wrong email", 401

@app.route('/singup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')
        users.append([login, email, password])
        with open('data.pickle', 'wb') as file:
            pickle.dump(users, file)
        return redirect(url_for('page2'))

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('page1'))

@app.route('/p1', methods=['GET'])
def page1():
    return render_template('page1.html')

@app.route('/p2', methods=['GET'])
def page2():
    return render_template('page2.html')

@app.route('/p3', methods=['GET'])
def page3():
    return render_template('page3.html', users=users)


#app.run(host="0.0.0.0", port=5000, debug='true')