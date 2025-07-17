from flask import Flask , render_template , request

app = Flask(__name__)

# by default these three methods are get method
# @app.route("/")
# def home() :
#     html = """<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     hello  this is the htmnl page 
# </body>
# </html>"""
#     return html

# @app.route ("/index")
# def index_html():
#     return render_template ("index.html")


# @app.route("/login")
# def login ():
#     return "this feature add in future "


@app.route("/name" , methods=["POST"])
def show ():
    name = request.form['Name']
    print (name)
    return "Success"

@app.route ("/getData" , methods=["GET"])
def getData ():
    name = "Sergio"
    return name


if __name__ == "__main__" :
    app.run (port=8000 , debug=True)