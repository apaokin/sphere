from flask import Flask

app = Flask(__name__)
Flask.g=0;
@app.route('/')
def hello_world():
    Flask.g+=1;
    return 'counter: ' + str(Flask.g)

if __name__ == '__main__':
    app.run()
