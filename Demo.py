from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('404.html')

@app.route('/user/<name>')
def user(name):
    return 'hello world!:'+name




if __name__ == '__main__':
    app.run(debug=True)