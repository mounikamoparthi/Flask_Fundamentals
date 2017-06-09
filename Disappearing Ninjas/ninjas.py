from flask import Flask, render_template, request, redirect
app = Flask(__name__)   #instantiation
@app.route('/')
def index():
    return render_template("index.html") 
@app.route('/ninja', methods = ['POST'])
def ninjas():
    return render_template("ninja.html")  
@app.route('/ninja/<ninja_color>')
def ninjacolor(ninja_color):
    print ninja_color
    return render_template("ninja.html",ninja_color = ninja_color )
app.run(debug=True) 