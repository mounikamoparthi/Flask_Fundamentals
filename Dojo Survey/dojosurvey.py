from flask import Flask, render_template, request, redirect
app = Flask(__name__)   #instantiation
@app.route('/')
def index():
    return render_template("index.html") 
@app.route('/process', methods=['POST'])
def Dojosurvey():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    return render_template("result.html",name=name,location=location,language=language)  
app.run(debug=True) 