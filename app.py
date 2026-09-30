from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

data = {
    "message": "Updated JSON from Rohit_new branch",
    "project": "Git and GitHub DEVOPS Assignment",
    "version": "2.0"
}

client = MongoClient("YOUR_MONGODB_CONNECTION_STRING")

db = client["todoDB"]
todo_collection = db["todoItems"]


@app.route("/")
def home():
    return "Flask Git & GitHub Assignment"


@app.route("/api")
def api():
    return jsonify(data)


@app.route("/todo")
def todo():
    return render_template("todo.html")


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():

    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    todo_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({
        "message": "To-Do item submitted successfully",
        "itemName": item_name,
        "itemDescription": item_description
    })


if __name__ == "__main__":
    app.run(debug=True)