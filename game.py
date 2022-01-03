from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def game():
    return render_template("fox_game.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)