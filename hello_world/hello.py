from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')
def success():
  return render_template('success.html')
@app.route('/index')
def index():
  return render_template('index.html')
app.run(debug=True)
