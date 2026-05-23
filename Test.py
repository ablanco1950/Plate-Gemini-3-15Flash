"""
Preguntando a la IA de google python code to recognize numbers licenses plates with gemini-3.5 flash
Modificado por Alfonso Blanco García 23/05/2026

Para reconocer placas de matrícula de vehículos mediante Gemini 3.5 Flash en Python, debes emplear el SDK oficial actualizado (google-genai). Este modelo procesa imágenes de forma nativa, lo que permite extraer el texto de la matrícula directamente actuando como un sistema OCR de alto rendimiento. [1, 2, 3, 4] 
           Requisitos previos
Primero debes instalar el SDK oficial de Google Gen AI junto con la librería Pillow para la manipulación de imágenes: [5, 6] 
pip install google-genai pillow

El siguiente script carga las imagen de vehículos de una carpeta en disco, l0s envía a gemini-3.5-flash con instrucciones precisas
y devuelve la matrícula limpia
"""

import os
# Fuerza la clave en el script (reemplaza con tu clave real)
os.environ["GEMINI_API_KEY"] = "Here_your_api_key"

import re

from google import genai
from PIL import Image

def reconocer_matricula(ruta_imagen: str) -> str:
    """
    Detecta y lee los caracteres de una placa de matrícula en una imagen
    utilizando el modelo multimodal Gemini 3.5 Flash.
    """
    # 1. Inicializar el cliente (recoge automáticamente GEMINI_API_KEY del entorno)
    client = genai.Client()
    
    # 2. Cargar la imagen del vehículo
    try:
        imagen = Image.open(ruta_imagen)
    except FileNotFoundError:
        return f"Error: No se encontró el archivo de imagen en '{ruta_imagen}'."
    except Exception as e:
        return f"Error al abrir la imagen: {e}"

    # 3. Definir un prompt específico para tareas de OCR automotriz
    prompt = (
        "Analiza la imagen de este vehículo e identifica la placa de matrícula "
        "(patente / licencia). Devuelve ÚNICAMENTE el texto alfanumérico legible "
        "de la matrícula. No incluyas explicaciones, ni el país, ni espacios extra."
    )

    # 4. Enviar la imagen y el prompt a Gemini 3.5 Flash
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=[imagen, prompt]
        )
        # Retornar la respuesta limpia removiendo saltos de línea basura
        return response.text.strip()
    except Exception as e:
        return f"Error al conectar con la API de Gemini: {e}"

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Sustituye por la ruta real de tu archivo de imagen (ej. 'auto.jpg')
    #archivo_vehiculo = "ruta/a/tu/foto_vehiculo.jpg"
    
  imgpath="Test1" # images test folder
  for root, dirnames, filenames in os.walk(imgpath):
   
 
   for filename in filenames:
     
    if re.search("\.(jpg|JPEG|jpeg|png|bmp|tiff)$", filename):
         
        
        filepath = os.path.join(root, filename)     
        archivo_vehiculo = filepath
    
        print("Procesando imagen con Gemini 3.5 Flash...")
        resultado = reconocer_matricula(archivo_vehiculo)
        
        print("\n==============================")
        print("Imagen " + filename)
        print(f"Matrícula detectada: {resultado}")
        print("==============================")
        input("PLEASE, PRESS ENTER TO CONTINUE...")

