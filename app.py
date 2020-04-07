from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Hunt!'


if __name__ == '__main__':
    app.run()
