from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/result",methods=["GET", "POST"])
def result():
    name = request.form["name"]
    year = request.form["year"]
    age = 2023-int(year)
    print(age)

    return render_template("result.html",name = name,age = age)

app.run(debug=True)