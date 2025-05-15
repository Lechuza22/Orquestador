# app/categorize.py

from joblib import load
import os

# Ruta al modelo entrenado
modelo_path = os.path.join(os.path.dirname(__file__), "modelo_categoria.pkl")

# Verificación y carga del modelo
try:
    modelo = load(modelo_path)
except FileNotFoundError:
    print("[!] No se encontró el archivo 'modelo_categoria.pkl'. Se usará fallback por palabra clave.")
    modelo = None

# Fallback simple en caso de que el modelo no esté
def fallback_categorizar(pregunta: str) -> str:
    pregunta = pregunta.lower()
    if any(p in pregunta for p in ["material", "cemento", "techos", "ladrillo"]):
        return "materiales"
    elif any(p in pregunta for p in ["precio", "costos", "cuánto"]):
        return "precios"
    elif any(p in pregunta for p in ["entrega", "envío", "logística"]):
        return "logística"
    else:
        return "otros"

# Función principal
def categorizar_consulta(pregunta: str) -> str:
    if modelo:
        return modelo.predict([pregunta])[0]
    else:
        return fallback_categorizar(pregunta)
