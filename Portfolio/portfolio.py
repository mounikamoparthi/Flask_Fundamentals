from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Hello_World():
     return render_template('index.html')


@app.route('/projects')
def myproj():
    return render_template('project.html')

@app.route('/about')
def AboutMe():
    return render_template('aboutme.html')
app.run(debug=True)