from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download")
def download():
    return render_template("download.html")


@app.route("/confirm")
def confirm():
    return render_template("confirm.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
