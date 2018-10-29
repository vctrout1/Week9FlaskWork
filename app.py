from flask import Flask, render_template
import random





app = Flask(__name__)

@app.route('/')

def index():
    names = ["Valeri", "Jin", "Bob"]
    return render_template("home.html", users=names)

@app.route('/about')
def about():
    return render_template("about.html")

app.run()