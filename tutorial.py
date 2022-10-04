from flask import Flask,redirect,url_for, render_template,request,session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "sing"
app.permanent_session_lifetime = timedelta(minutes=15)


@app.route("/")   #name is being passed in from the url end point 
def home():
    return render_template("index.html")


@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1> "
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    #return redirect(url_for("home"))
    return render_template("logout.html")



if __name__ == "__main__":
    app.run(debug=True)
