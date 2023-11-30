from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime



import pymongo


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Conexión a MongoDB Atlas
uri = "mongodb+srv://figueroa:agosto07@ejemplo.ppbsen6.mongodb.net/huertoutc?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client.huertoutc


coleccion_Materias = db.Materias
coleccion_alumnos = db.Alumno

print("Obteniendo AlumnoS...")

@app.route("/api/alumno", methods=["GET"])
def obtener_alumnos():
    try:
        # Agregar mensaje de impresión para verificar que se está obteniendo la lista de plantas
        print("Obteniendo la lista de alumnos...")

        # Obtiene todas las plantas de la colección
        alumnos = list(coleccion_alumnos.find({}, {"_id": 0}))  # Excluye el campo _id

        # Agregar mensaje de impresión para verificar que se obtuvo la lista de plantas correctamente
        print("Lista de alumnos obtenida")

        return jsonify(alumnos)
    except Exception as e:
        # En caso de error, imprimirlo en la consola
        print("Error al obtener la lista de alumnos:", str(e))
        return jsonify({"error": "Ocurrió un error al obtener alumnos"}),500


#Api de materias

if __name__ == "__main__":
    app.run()
