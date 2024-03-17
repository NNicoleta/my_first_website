from flask import Flask, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__)

DB_PATH = 'nou3.db'

form_submitted = False
show_rounds = False


def insert_data(first_name, last_name, email, firm, domain, message):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO web (first_name, last_name, email, firm, domain, message) VALUES (?, ?, ?, ?, ?, ?)",
              (first_name, last_name, email, firm, domain, message))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html", show_form=False, form_submitted=form_submitted, show_rounds=show_rounds)

@app.route("/index", methods=["POST"])
def submit():
    global form_submitted

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    firm = request.form['firm']
    domain = request.form['domain']
    message = request.form['message']

    insert_data(first_name, last_name, email, firm, domain, message)

    form_submitted = True
    return redirect(url_for('home'))

@app.route("/form")
def render_form():

    global form_submitted
    form_submitted = False
    return render_template("index.html", show_form=True, form_submitted=False, show_rounds=show_rounds)

@app.route("/start")
def toggle_rounds():
    global show_rounds

    show_rounds = not show_rounds
    return redirect(url_for('home'))

@app.route("/login")
def render_login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
