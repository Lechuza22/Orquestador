# app/categorize.py

import os
import logging
from joblib import load

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="🧩 %(levelname)s | %(message)s"
)

# Ruta del modelo entrenado
modelo_path = os.path.join(os.path.dirname(__file__), "modelo_categoria.pkl")

# Intentar cargar el modelo entrenado
try:
    modelo = load(modelo_path)
    logging.info("Modelo de categorización cargado correctamente.")
except FileNotFoundError:
    modelo = None
    logging.warning("No se encontró el modelo 'modelo_categoria.pkl'. Usando fallback por palabras clave.")

# Función de fallback con reglas básicas
def fallback_categorizar(pregunta: str) -> str:
    pregunta = pregunta.lower()
    if any(p in pregunta for p in ["material", "cemento", "techos", "ladrillo"]):
        return "materiales"
    elif any(p in pregunta for p in ["precio", "costos", "cuánto", "vale"]):
        return "precios"
    elif any(p in pregunta for p in ["entrega", "envío", "logística", "reparto"]):
        return "logística"
    else:
        return "otros"

# Función principal
def categorizar_consulta(pregunta: str) -> str:
    logging.debug(f"Consulta recibida para categorizar: '{pregunta}'")

    if modelo:
        categoria = modelo.predict([pregunta])[0]
        logging.info(f"Categoría predicha por el modelo: {categoria}")
        return categoria
    else:
        categoria = fallback_categorizar(pregunta)
        logging.info(f"Categoría determinada por fallback: {categoria}")
        return categoria
