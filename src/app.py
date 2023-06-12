from flask import Flask, render_template, request
import urllib.request

app = Flask(__name__)

@app.route("/")
def home():
    title = 'Home'
    return render_template('index.htm', title = title)

@app.route("/academico")
def academico():
        title = 'Acadêmico'
        return render_template('academico.htm', title = title)

@app.route("/pessoal")
def pessoal():
        title = 'Pessoal'
        return render_template('pessoal.htm',title = title)

@app.route("/contatos")
def sobre():
    title = 'Contatos'
    return render_template('contatos.htm', title = title)

if __name__ == '__main__':
    app.run()