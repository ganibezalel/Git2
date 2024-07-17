from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi, world!'

if __name__ == '__main__':
    app.run()

