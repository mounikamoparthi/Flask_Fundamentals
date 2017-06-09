from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'hebflbbdvdbf'
def sumSession(i):
    try:
        session['counter'] += i 
    except KeyError:
        session['counter'] = 1
    return session['counter']
@app.route('/')
def index():
    print session['counter']
    return render_template("index.html", counter =sumSession(1))
@app.route ('/result', methods = ['POST'])
def res():
    print 'counter'
    return render_template("result.html", counter = sumSession(2))
app.run(debug=True) 
  