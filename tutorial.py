import re
from selectors import EpollSelector
from flask import Flask,redirect,url_for, render_template,request,session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "sing"
app.permanent_session_lifetime = timedelta(minutes=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


    def __init__(self,name,email):
        self.name = name
        self.email = email

@app.route("/")   #name is being passed in from the url end point 
def home():
    return render_template("home.html")


@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Redirect already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email 
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        #return f"<h1>{user}</h1> 
        return render_template("user_page.html", user=user,email=email) # passing the variable user into the html file
    else:
        flash("Not logged in, please login!")
        return redirect(url_for("login"))

   


@app.route("/logout")
def logout():
    # if "user" in session:
    #     user = session["user"]
    user = session["user"]
    flash(f"You have been logged out","info")
    session.pop("user", None)
    session.pop("email", None)

    return render_template("logout.html", user=user)


@app.route("/sample")
def sample():
    return render_template("sample.html", values=users.queries.all())


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
