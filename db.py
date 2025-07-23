from flask import Flask , render_template , request , redirect 


server = Flask(__name__)

@server.route ("/")
def home ():
    return render_template("db/index.html")

server.run (port=8000 , debug=True)