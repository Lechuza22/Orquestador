# app/orchestrator.py

from langchain.schema.runnable import RunnableMap, RunnableSequence
from search_docs import buscar_documentos_relevantes
from generate_response import generar_respuesta_con_gemini
from categorize import categorizar_consulta
from context_initializer import cargar_contexto_desde_yaml


# --- Cargar y validar contexto inicial desde YAML ---
contexto_inicial = cargar_contexto_desde_yaml()

def tipo_de_contexto(ctx: dict) -> str:
    if not ctx:
        return "vacío"
    elif any(isinstance(v, (dict, list)) for v in ctx.values()):
        return "complejo"
    else:
        return "simple"

print(f"[✓] Contexto inicial detectado ({tipo_de_contexto(contexto_inicial)}):\n{contexto_inicial}")


# --- Construcción de prompt ---
def construir_prompt(pregunta, fragmentos, categoria, contexto_extra=None):
    contexto_docs = "\n\n".join([doc.page_content for doc in fragmentos]) if fragmentos else "No se encontró contenido relevante."
    contexto_yaml = f"Contexto del workflow:\n{contexto_extra}" if contexto_extra else ""
    
    return f"""Categoría: {categoria}
{contexto_yaml}

Contexto documental:
{contexto_docs}

Pregunta:
{pregunta}

Instrucciones: Respondé usando solo la información proporcionada. Si no hay suficiente contexto, indicá que no es posible responder con precisión.
"""

# --- Definición del pipeline orquestado ---
def inicializar_orquestador():
    return RunnableSequence(
        RunnableMap({
            "pregunta": lambda input: input["pregunta"],
            "categoria": lambda input: categorizar_consulta(input["pregunta"]),
            "fragmentos": lambda input: buscar_documentos_relevantes(input["pregunta"]),
            "contexto": lambda _: contexto_inicial,
        }),
        lambda entrada: {
            "respuesta": generar_respuesta_con_gemini(
                entrada["pregunta"],
                entrada["fragmentos"],
                prompt_personalizado=construir_prompt(
                    entrada["pregunta"],
                    entrada["fragmentos"],
                    entrada["categoria"],
                    entrada["contexto"]
                )
            )
        }
    )
