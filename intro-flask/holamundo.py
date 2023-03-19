from flask import Flask

app = flask(__name__)  # este valor va ser main cuando usemos el archivo


@app.route('/')
def index():
    return 'hola mundo'
