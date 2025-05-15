# app/categorize.py

def categorizar_consulta(pregunta: str) -> str:
    pregunta = pregunta.lower()

    if any(palabra in pregunta for palabra in ["material", "materiales", "cemento", "ladrillo", "techos"]):
        return "materiales"
    elif any(palabra in pregunta for palabra in ["precio", "costos", "cuánto", "vale", "vale la pena"]):
        return "precios"
    elif any(palabra in pregunta for palabra in ["logística", "envío", "entrega", "tiempo", "demora"]):
        return "logística"
    else:
        return "otros"
