# My Image Processing API

API simple de Flask, recibe una imagen y regresa información sobre esta en un JSON 

## Dependencias
El proyecto usa las paqueterías de python: 

Flask==3.0.3
numpy==2.0.0
pillow==10.4.0

## instalación
Para instalar el proyecto debe seguir los siguientes pasos

1. **clonar el repositorio**:
    ```sh
    git clone https://github.com/HanniaTanil/api-imagenes
    cd api-imagenes
    ```

2. **Crear un ambiente virtual**:
    ```sh
    python -m venv myenv
    ```

3. **Activar el ambiente virtual**:
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source myenv/bin/activate
        ```

4. **Instalar las dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

## Correr la aplicación

```sh
python api.py


##Probar la api
```sh
python api-test.py
