from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Users/seelamakhil/flask/templates/home.html')
def home():
    return render_template('home.html')

@app.route('/Users/seelamakhil/flask/templates/data.html')
def data():
    return render_template('data.html')

@app.route('/Users/seelamakhil/flask/templates/dashboards.html')
def dashboards():
    return render_template('dashboards.html')

@app.route('/Users/seelamakhil/flask/templates/cognos.html')
def cognos():
    return render_template('cognos.html')

if __name__ == '__main__':
    app.run(debug=True)
