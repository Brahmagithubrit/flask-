from flask import Flask , render_template , request

app = Flask (__name__ )

@app.route("/")
def home ():
    return render_template("index2.html")

@app.route ("/name" , methods=["POST"])
def show ():
    name = request.form["name"]
    custom_message  = f"Welcome ${name} to our website "
    return render_template("index2.html", Message = custom_message )

app.run (port=8000 , debug=True )