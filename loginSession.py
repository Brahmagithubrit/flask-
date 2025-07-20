from flask import Flask , render_template , request , session ,  redirect
from  werkzeug.security import check_password_hash , generate_password_hash

app = Flask (__name__)
app.secret_key = "Secret"

@app.route("/")
def home ():
    # if "name" in session :
    #     return redirect("/dashboard")   #this should off for login 
    return render_template("loginSession/index.html")


@app.route("/register" , methods=["POST"])
def register ():
    name = request.form["name"]
    hashed_name = generate_password_hash(name)
    # storage in sesion 
    session["name"] = hashed_name
    print (session)
    return redirect ("/dashboard")

@app.route ("/login" , methods=["POST"])
def login ():
    if "name" not in session :
        return render_template("/loginSession/index.html" ,  message ="Id not exist")
    else :
        hashed_name = session["name"]
        name = request.form["name2"]
        if check_password_hash(hashed_name , name ):
            return redirect("/dashboard")
        else :
            return render_template("/loginSession/index.html" , message = "Wrong Cred")

@app.route("/dashboard")
def dashboard():
    if "name" in session:
        return render_template("loginSession/dashboard.html")
    else : return render_template ("loginSession/index.html")


@app.route("/logout")
def logout():
    session.pop("name")
    return redirect("/")

app.run (port=8000 , debug=True )