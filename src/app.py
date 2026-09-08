"""Aplicación deliberadamente vulnerable para una demo de CodeQL.

NO USAR EN PRODUCCIÓN.
"""

import sqlite3
from flask import Flask, request

app = Flask(__name__)


def find_user_by_id(user_id: str):
    """Ejemplo intencional de SQL Injection.

    Source: request.args.get("id") en el endpoint.
    Sink: cursor.execute(query).
    """
    connection = sqlite3.connect("demo.db")
    cursor = connection.cursor()

    # VULNERABLE A PROPÓSITO: concatena entrada no confiable en SQL.
    query = "SELECT id, username FROM users WHERE id = " + user_id
    cursor.execute(query)

    result = cursor.fetchall()
    connection.close()
    return result


@app.get("/user")
def get_user():
    user_id = request.args.get("id", "0")
    return {"results": find_user_by_id(user_id)}


if __name__ == "__main__":
    # La aplicación solo escucha en localhost para reducir el riesgo accidental.
    app.run(host="127.0.0.1", port=5000, debug=False)
