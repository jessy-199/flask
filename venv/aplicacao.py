from flask import Flask

app = Flask(__name__)

@app.route('/estrela')

def ola():
    return '<h1>my friend!</h1>'


app.run()
