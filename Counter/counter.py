from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'hebflbbdvdbf'
def sumSession():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    return session['counter']
@app.route('/')
def index():
    return render_template("index.html", counter =sumSession())
app.run(debug=True) 