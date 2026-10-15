import random
from flask import Flask, request, jsonify

ROLL_NUMBER = "FA23-BDS-017"

# Coefficients generated deterministically from the roll number seed
random.seed(ROLL_NUMBER)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)


@app.route("/predict")
def predict():
    x1 = float(request.args.get("x1", 0))
    x2 = float(request.args.get("x2", 0))
    x3 = float(request.args.get("x3", 0))
    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({
        "registration number": ROLL_NUMBER,
        "prediction": round(y, 2)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
