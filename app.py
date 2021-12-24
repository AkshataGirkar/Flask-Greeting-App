from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)
app.secret_key = "qwer5273839_26g"

@app.route("/hello")
def index():
	flash("What's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hii " + str(request.form['name_input']) + ", great to see you!!")
	return render_template("index.html")






# if __name__ == "__main__":
# 	app.run(debug=True)