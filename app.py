from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Conexión a la BD
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Usuario por defecto en XAMPP
        password="",        # Vacío por defecto
        database="tienda"
    )

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    tipo = request.args.get('tipo')
    categoria = request.args.get('categoria')
    orden = request.args.get('orden')

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM productos WHERE 1=1"

    if tipo and tipo != 'todos':
        query += f" AND tipo = '{tipo}'"

    if categoria and categoria != 'todos':
        query += f" AND categoria = '{categoria}'"

    if orden == 'precio-asc':
        query += " ORDER BY precio ASC"
    elif orden == 'precio-desc':
        query += " ORDER BY precio DESC"
    elif orden == 'mejor-valorados':
        query += " ORDER BY valoracion DESC"
    elif orden == 'recientes':
        query += " ORDER BY fecha DESC"

    cursor.execute(query)
    productos = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(productos)

if __name__ == '__main__':
    app.run(debug=True)
