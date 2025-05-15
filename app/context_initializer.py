# app/context_initializer.py

import yaml
import os

def cargar_contexto_desde_yaml(path="workflow.yaml"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"[!] No se encontró el archivo de configuración YAML en: {path}")

    with open(path, "r", encoding="utf-8") as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"[!] Error al parsear el archivo YAML: {e}")

    context_node = config.get("nodes", {}).get("Context Initial")
    if context_node is None:
        print("[!] Nodo 'Context Initial' no definido. Se usará contexto vacío.")
        return {}

    context_data = context_node.get("context", {})

    if not isinstance(context_data, dict):
        raise TypeError("[!] La clave 'context' del nodo 'Context Initial' debe ser un diccionario.")

    return context_data
