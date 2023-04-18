from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

app.route("/")
def home():
    return render_template("index.html")

app.route("/minhasinformacoes")
def minhasinformacoes():
    return render_template("minhasinformacoes.html")

app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == '__main__':
    app.run()