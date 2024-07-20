from flask import Flask, request, jsonify
from PIL import Image
import io
import numpy as np

app = Flask(__name__)

def analizar_imagen(imagen):
    # Análisis de ejemplo: regresa el ancho y alto de la imagen
    width, height = imagen.size
    return {
        "ancho": width,
        "alto": height
    }
#Se define el endpoint
@app.route('/subir', methods=['POST'])
def subir_imagen():
    if 'archivo' not in request.files:
        return jsonify({"error": "No hay archivo"}), 400

    archivo = request.files['archivo']
    if archivo.filename == '':
        return jsonify({"error": "No hay archivo seleccionado"}), 400

    try:
        imagen = Image.open(archivo.stream)
        resultado = analizar_imagen(imagen)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
