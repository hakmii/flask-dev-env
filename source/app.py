from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/info')
def info():
    return 'Here comes some info!'

@app.route('/autodeploy')
def autodeploy():
    return 'It just works?'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
