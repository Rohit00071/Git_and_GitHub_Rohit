from flask import Flask, jsonify, render_template

app = Flask(__name__)

data = {
    "message": "Updated JSON from Rohit_new branch",
    "project": "Git and GitHub DEVOPS Assignment",
    "version": "2.0"
}


@app.route("/")
def home():
    return "Flask Git & GitHub Assignment"


@app.route("/api")
def api():
    return jsonify(data)


@app.route("/todo")
def todo():
    return render_template("todo.html")


if __name__ == "__main__":
    app.run(debug=True)