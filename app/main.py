# app/main.py

import os
from orchestrator import inicializar_orquestador

# Inicializar el pipeline de LangChain
pipeline = inicializar_orquestador()

print("🧠 LLM Categorizer con Orquestador YAML")
print("🔍 Ingresá tu pregunta (o escribí 'salir'):")

while True:
    pregunta = input("> ")

    if pregunta.strip().lower() == "salir":
        print("👋 ¡Hasta la próxima!")
        break

    if not pregunta.strip():
        print("⚠️ Ingresá una pregunta válida.")
        continue

    try:
        resultado = pipeline.invoke({"pregunta": pregunta})
        print("\n📌 Respuesta generada por Gemini:")
        print(resultado["respuesta"])
    except Exception as e:
        print(f"[Error durante la ejecución]: {e}")
