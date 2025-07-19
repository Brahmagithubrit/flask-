from flask import Flask, render_template, request
import time
app = Flask(__name__)

username = "User"
tasks = []
idx = 0

@app.route("/")
def intro():
    return render_template("index.html")

@app.route("/name", methods=["POST"])
def home():
    time.sleep(3)
    name = request.form["name"]
    global username
    username = name 
    return render_template("todo/index2.html", name=name, tasks=tasks)

@app.route("/task", methods=["POST"])
def add_task():
    global idx
    idx += 1
    task_text = request.form["task"]

    task = {
        "id": idx,
        "task": task_text
    }

    tasks.append(task)
    return render_template("todo/index2.html",name = username , tasks=tasks)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    global tasks
    updated_tasks = []

    for t in tasks:
        if t["id"] != id:
            updated_tasks.append(t)

    tasks = updated_tasks
    return render_template("todo/index2.html", name = username  , tasks=tasks)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
