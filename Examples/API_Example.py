from flask import Flask

app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hi How are you doing today?"


@app.route('/v1/api/login', methods=['GET', 'POST'])
def login_validation():
    return "You have successfully logged In"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8087)
