from flask import Flask,flash,render_template, request, redirect,session
app = Flask(__name__)   #instantiation
app.secret_key = 'keepitsecret'
@app.route('/')
def index():
    return render_template("index.html") 
@app.route('/process', methods=['POST'])
def Dojosurvey():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    if len(request.form['language']) < 1:
        flash("language cannot be empty!")
    else:
        flash("Success! Your favlanguage is {}".format(request.form['language']))
    return redirect('/')
    print request.form
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    return render_template("result.html",name=name,location=location,language=language)  
@app.route('/back', methods =['POST'])
def backpage():
    index()
    return redirect('/')
app.run(debug=True) 