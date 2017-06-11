from flask import Flask,flash, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'abhbbibi'
def setSession():
    session['computer_input']=random.randint(1,100) 
@app.route('/')
def index():
    try:
        session['computer_input'] 
    except KeyError:
        setSession()

    print session['computer_input']
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def game():
    num = request.form ['number']
    right = None
    wrong = None
    if int(num) == session['computer_input']:
        flash( "Play again", 'right')
        return redirect('/')
    elif int(num) > session['computer_input']:
        flash( "Too High!", 'toohigh')
    elif int(num) < session['computer_input']:
        flash ("Too Low!", 'toolow')
    else:
        flash('error', 'wrong')
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    setSession()
    return redirect('/')

app.run(debug = True)