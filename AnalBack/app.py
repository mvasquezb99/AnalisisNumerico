from flask import Flask, jsonify, request
from flask_cors import CORS
from metodos import (
    biseccion,
    mod1_newton,
    mod2_newton,
    newton,
    punto_fijo,
    regla_falsa,
    secante,
)

app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/biseccion", methods=["GET", "POST"])  # type: ignore
def biseccion_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "a": "",
                "b": "",
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        a = float(request.get_json()["input"]["a"])
        b = float(request.get_json()["input"]["b"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        result = biseccion.bisec(fx, a, b, tol, n_iter)
        return result


@app.route("/reglaFalsa", methods=["GET", "POST"])  # type: ignore
def regla_falsa_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "a": "",
                "b": "",
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        a = float(request.get_json()["input"]["a"])
        b = float(request.get_json()["input"]["b"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        return regla_falsa.regla_falsa(
            fx, a, b, tol, n_iter
        )  # TODO: Check thath the method is correct


@app.route("/puntoFijo", methods=["GET", "POST"])
def punto_fijo_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "g": "",
                "x0": "",
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        g = request.get_json()["input"]["g"]
        x0 = float(request.get_json()["input"]["x0"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        return punto_fijo.pf(fx, g, x0, tol, n_iter)


@app.route("/newton", methods=["GET", "POST"])
def newton_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        return newton.nt(fx, x0, tol, n_iter)


@app.route("/secante", methods=["GET", "POST"])
def secante_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "x1": "",
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        x1 = float(request.get_json()["input"]["x1"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        return secante.seca(fx, x0, x1, tol, n_iter)


@app.route("/newton_mod1", methods=["GET", "POST"])
def newton_mod1_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "m": "",
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        m = float(request.get_json()["input"]["m"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        return mod1_newton.mnt(fx, m, x0, tol, n_iter)


@app.route("/newton_mod2", methods=["GET", "POST"])
def newton_mod2_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        return mod2_newton.mnt(fx, x0, tol, n_iter)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
