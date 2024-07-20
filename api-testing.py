import requests

url = 'http://127.0.0.1:5000/subir'
ruta_archivo = "C:/Users/hanni/OneDrive/Pictures/comb3.png"

with open(ruta_archivo, 'rb') as file:
    archivos = {'archivo': file}
    respuesta = requests.post(url, files=archivos)

print(respuesta.json())
