# LLM Categorizer con Orquestador y Clasificación Inteligente

Este proyecto es una demo funcional de un sistema inteligente que responde consultas en lenguaje natural basándose en documentos cargados por el usuario. Integra recuperación semántica, clasificación automática y generación de respuestas con el modelo Gemini 1.5 de Google.

## Funcionalidad principal

- Carga de documentos `.txt` o `.pdf` desde `data/documentos_raw/`.
- Fragmentación y vectorización con embeddings de Hugging Face (`all-MiniLM-L6-v2`).
- Indexación con FAISS para búsqueda semántica.
- Clasificación automática de la intención de la consulta (materiales, precios, logística, etc.).
- Orquestador basado en YAML que inicializa el contexto del flujo.
- Generación de respuesta contextualizada usando `gemini-2.0-flash` vía REST API.

## Estructura de archivos

```
SistCategorización/
├── app/
│   ├── main.py                  # Interfaz por consola
│   ├── orchestrator.py          # Flujo de ejecución con LangChain
│   ├── context_initializer.py   # Carga de contexto desde workflow.yaml
│   ├── categorize.py            # Clasificador de intención con fallback
│   ├── generate_embeddings.py   # Procesamiento de documentos y FAISS
│   ├── search_docs.py           # Búsqueda de fragmentos relevantes
│   ├── generate_response.py     # Llamada a Gemini con prompt personalizado
│   └── config.py                # Carga de clave desde .env
├── data/documentos_raw/        # Documentos de entrada
├── vectorstore/                # Almacenamiento del índice FAISS
├── workflow.yaml               # Definición del nodo Context Initial
├── requirements.txt
└── .env                        # Clave de API: GEMINI_API_KEY
```

## Cómo usarlo

1. Crear `.env` con:

   ```
   GEMINI_API_KEY=tu_clave_gemini
   ```

2. Asegurarse de tener documentos en `data/documentos_raw/`.

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Entrenar el clasificador (opcional):

   Ejecutar `Entrenamiento_Categorizador.ipynb` y guardar `modelo_categoria.pkl` en `/app`.

5. Ejecutar:

   ```bash
   cd app
   python main.py
   ```

6. Escribir una pregunta y recibir la respuesta generada por Gemini con contexto.

## Context Initial Orchestrator

El flujo se configura desde `workflow.yaml`, permitiendo:

- Iniciar con contexto simple o complejo
- Compartir datos iniciales con el pipeline
- Controlar el comportamiento de generación según la configuración

## Ejemplo de contexto en YAML

```yaml
nodes:
  Context Initial:
    context:
      cliente: "Customer A"
      categoria: "materiales"
      prioridad: "alta"
```

## Categorías actuales

- materiales
- precios
- logística
- otros

Si no se encuentra el modelo entrenado, se usa una heurística por palabras clave como fallback.
