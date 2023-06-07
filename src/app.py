from flask import Flask, render_template, request
import urllib.request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.htm')

@app.route("/academico")
def academico():
        return render_template('academico.htm')

@app.route("/pessoal")
def pessoal():
        return render_template('pessoal.htm')

@app.route("/sobre")
def sobre():
    return render_template('sobre.htm')

if __name__ == '__main__':
    app.run()