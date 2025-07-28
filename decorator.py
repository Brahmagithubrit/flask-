from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)


# decorator is basically do a validation on data before move forward 
# it simply use wrap and method inside another method to validate
# we can use our cusotm decoration for validate the data 
def validate_user(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        user = request.get_json()

        if not user:
            return jsonify({"error": "User data is missing"})

        name = user.get("name")
        password = user.get("password")

        if not name:
            return jsonify({"error": "Name is required"})
        if not password or len(password) <= 4:
            return jsonify({"error": "Password must be more than 4 characters"})

        return f(*args, **kwargs)
    return decorator

@app.route("/")
def home():
    return "Home"

@app.route("/signup", methods=["POST", "PUT"])
@validate_user
def signup():
    user = request.get_json()
    # You can now safely use user["name"] and user["password"]
    return jsonify({"success": "Signup successful!"})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
