from flask import Flask, request, jsonify
import time
import random
import string

app = Flask(__name__)

# Generate a random password
symbols = "!@#$%&*+-=()[]{}"
PASSWORD = ''.join(random.choice(string.ascii_letters + string.digits + symbols) for _ in range(32))
print(f"Generated Password: {PASSWORD}")

@app.route("/auth_password", methods=["POST"])
def auth_password():
    user_input = request.json.get("password", "")

    print(f"Received: {user_input}")

    # compare length
    if len(user_input) != len(PASSWORD):
        return jsonify({"result": False})

    # compare each character
    for i in range(len(PASSWORD)):
        time.sleep(0.005)  # wait 5ms
        if PASSWORD[i] != user_input[i]:
            return jsonify({"result": False})

    # correct password
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(port=5000)
