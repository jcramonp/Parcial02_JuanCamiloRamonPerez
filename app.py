from flask import Flask, jsonify, abort
import math

app = Flask(__name__)

def compute_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser >= 0")
    return math.factorial(n)

@app.get("/factorial/<int:n>")
def factorial(n: int):
    try:
        f = compute_factorial(n)
    except ValueError as e:
        abort(400, description=str(e))
    etiqueta = "par" if n % 2 == 0 else "impar"
    return jsonify({"numero": n, "factorial": f, "etiqueta": etiqueta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
