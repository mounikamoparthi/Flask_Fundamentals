from flask import Flask, render_template, request, redirect
app = Flask(__name__)   #instantiation
@app.route('/')
def index():
    return render_template("index.html") 
@app.route('/ninja')
def ninjas():
    return render_template("ninja.html")  
app.run(debug=True) 