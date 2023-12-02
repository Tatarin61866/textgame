from flask import Flask, request, render_template, flash, redirect, url_for, abort
from datetime import datetime

app = Flask('lab08')
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/page1', methods=['GET', 'POST'])
def page2():
    return render_template('page3.html')

@app.route('/page4', methods=['GET', 'POST'])
def page5():
    return render_template('page6.html')

@app.route('/go_to_index')
def redir():
    p = request.args.get('pass')
    if p != '123':
        return abort(403)
    return redirect(url_for('index'))

@app.route('/send_msg', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        m = request.form.get('text')
        flash(m)
    return render_template('form.html')

#app.run(host="0.0.0.0", port=5000, debug='true')