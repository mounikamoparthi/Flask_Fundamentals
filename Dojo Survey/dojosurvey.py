from flask import Flask,flash,render_template, request, redirect,session
app = Flask(__name__)   #instantiation
app.secret_key = 'keepitsecret'
@app.route('/')
def index():
    return render_template("index.html") 
@app.route('/process', methods=['POST'])
def req():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    if len(request.form['comment']) < 1:
        flash("comment cannot be empty!")
    elif len(request.form['comment']) > 120:
        flash("Exceeded 120 characters")
    return redirect('/')
@app.route('/process', methods=['POST'])
def Dojosurvey():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html",name=name,location=location,language=language, comment=comment)    
@app.route('/back', methods =['POST'])
def backpage():
    index()
    return redirect('/')
app.run(debug=True) 