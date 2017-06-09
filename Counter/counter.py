from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'hebflbbdvdbf'
def sumSession(i):
    try:
        session['counter'] += i 
    except KeyError:
        session['counter'] = 0
    return session['counter']
@app.route('/')
def index():
    return render_template("index.html", counter =sumSession(1))
@app.route ('/result', methods = ['POST'])
def res():
    return render_template("index.html", counter = sumSession(2))
@app.route('/clear', methods = ['POST'])
def clearing():
    try:
        session['counter'] = 0
    except ValueError:
        session['counter'] = 0
    return render_template("index.html", counter = session['counter'])
app.run(debug=True) 

  