from flask import Flask

app = Flask(__name__)

@app.route('/zhouyujia')
def hello():
    return 'zhouyujia01-- hello word!'

if __name__ == '__main__':
    app.run()