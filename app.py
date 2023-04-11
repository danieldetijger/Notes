from flask import Flask, redirect, request, render_template, session, send_file
from flask_session import Session
from cs50 import SQL
import sqlite3
import pandas
import csv
import datetime
from helpers import login_required, apology
from werkzeug.security import check_password_hash, generate_password_hash


#Initialize database
db = SQL("sqlite:///notes.db")

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#Main page
@app.route("/", methods = ["GET"])
@login_required
def home():
    user_id = session["user_id"]
    notes = db.execute("SELECT * FROM notes WHERE user_id = ?", user_id)
    number_of_notes = db.execute("SELECT COUNT(*) FROM notes WHERE user_id = ?", user_id)
    return render_template("home.html", notes = notes)

#Page on which data for new notes is entered, data will be passed to the homepage via POST.
@app.route("/new", methods = ["POST"])
@login_required
def new():
    user_id = session["user_id"]
    title = request.form.get("title")
    text = request.form.get("text")
    date = datetime.datetime.now()
    db.execute("INSERT INTO notes (title, text, date, user_id) VALUES (?, ?, ?, ?)", title, text, date, user_id)
    return redirect("/")

@app.route("/update", methods = ["POST"])
@login_required
def update():
    user_id = session["user_id"]
    title = request.form.get("title")
    text = request.form.get("text")
    note_id = request.form.get("note_id")
    date = datetime.datetime.now()    

    if title == text == "":
        db.execute("DELETE FROM notes WHERE note_id = ?", note_id)
    else:
        db.execute("UPDATE notes SET title = ?, text = ?, date = ? WHERE note_id = ?", title, text, date, note_id) 
    
    print(user_id, title, text, date, note_id)

    return redirect("/")

@app.route("/export", methods = ["GET"])
@login_required
def export():
    user_id = session["user_id"]
    notes = db.execute("SELECT * FROM notes WHERE user_id = ?", user_id)
    fields = ["note_id", "title", "text", "date", "user_id"]
    with open('out.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        for dictionary in notes:
            writer.writerow(dictionary.values())
    path = "C:/Users/Daniel.PC-DN/Desktop/project/Notes/out.csv"
    return send_file(path, as_attachment=True)

@app.route("/import", methods = ["GET", "POST"])
@login_required
def importf():
    user_id = session["user_id"]

    if request.method == "GET":
        return render_template("import.html")
    else:
        #Ask for file upload
        f = request.files['file']
        f.save(f.filename)
        with open(f.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                count = db.execute("SELECT COUNT(*) FROM notes WHERE note_id = ? LIMIT 1", row["note_id"])
                print(count)
                print(count[0]["COUNT(*)"])
                num = int(count[0]["COUNT(*)"])
                print(num)
                if num < 1:
                    db.execute("INSERT INTO notes(title, text, date, user_id) VALUES (?, ?, ?, ?)", row["title"], row["text"], row["date"], row["user_id"])
                else:
                    print("Present in DB")
        return redirect("/")


#Only account/session base code from here. DO NOT CHANGE

#Register new user
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("Input a username")
        if not password:
            return apology("Input a password")
        if not confirmation:
            return apology("Must confirm")
        if password != confirmation:
            return apology("Pass doesn't match confirmation")
        hash = generate_password_hash(password)
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username already exists")
        session["user_id"] = new_user
        return redirect("/")

#Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


#Logout route
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

