from flask import Flask,redirect,url_for, render_template

app = Flask(__name__)

@app.route("/")   #name is being passed in from the url end point 
def home():
    return render_template("index.html")


@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)
