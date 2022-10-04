from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello this is a sample"

@app.route("/home")
def home():
    return "Hello this is a sample2"

@app.route("/admin")

def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
