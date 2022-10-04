from flask import Flask,redirect,url_for, render_template

app = Flask(__name__)

@app.route("/<name>")   #name is being passed in from the url end point 
def home(name):
    return render_template("index.html", content=["quin","bill","tom"])


if __name__ == "__main__":
    app.run()
