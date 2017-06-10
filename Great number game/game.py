from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
@app.route('/')
def index():
    print "Hello I'am ready"
    return render_template('index.html')
app.run(debug = True)