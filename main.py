from flask import Flask, render_template, request, redirect
from flask.helpers import url_for

app = Flask(__name__)

total_count = 0


@app.route("/")
def hello_world():
    return "GO TO <a href='/count'>Click</a>"


@app.route("/count", methods=['POST', 'GET'])
def count():
    title = "Count"
    global total_count
    if request.method == "POST":
        if request.form.get("like") == "like":
            print("Like Pressed")
            total_count += 1
            return redirect(url_for('count'))
        if request.form.get("dislike") == "dislike":
            print("DisLike Pressed")
            total_count -= 1
            return redirect(url_for('count'))
    return render_template("main.html", count=total_count)


if __name__ == "__main__":
    app.debug = True
    app.run()
