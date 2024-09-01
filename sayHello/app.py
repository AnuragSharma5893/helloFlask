from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "sdkfj sdkiu jfkdsjfkjsa"

@app.route("/hello")
def index():
    #flash("What is your name?")
    return render_template("index.html")


@app.route("/greet", methods = ["POST", "GET"])
def greet():
    flash("Hii! " + str(request.form['name_input']) + ", greet to see you man!!")
    return render_template("index.html")
